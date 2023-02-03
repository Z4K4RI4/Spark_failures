# Spark_failures
## Objectif
Ce projet a pour but de tester différents scénarios de panne sur un cluster Spark.
## Comment utiliser ce projet
### Prérequis
* Docker et Docker-compose installés
* Télécharger le projet  
```$ git clone https://github.com/Z4K4RI4/Spark_failures.git```
* Se placer dans le dossier du projet  
```$ cd Spark_failures```
#### Préparation de Spark et Hadoop
##### Avec le script de configuration
* le fichier config.sh permet de réaliser le téléchargement de Spark et Hadoop, et de configurer les fichiers de configuration.
```./config.sh```
#### Manuellement
* Télécharger les archives de Spark et Hadoop  
```$ wget "https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz" && tar -xvf hadoop-3.3.3.tar.gz && rm hadoop-3.3.3.tar.gz```  
```$ wget "https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz" && tar -xvf spark-3.3.1-bin-hadoop3.tgz && rm spark-3.3.1-bin-hadoop3.tgz```  
* Modifier les fichiers de configuration de Spark et Hadoop  
    * Copie des fichiers de configuration de Hadoop :  
    ```$ cp ressources/configurations_files/hadoop/* hadoop-3.3.3/etc/hadoop/```  
    * Copie des fichiers de configuration de Spark :  
    ```$ cp ressources/configurations_files/spark/* spark-3.3.1-bin-hadoop3/conf/```
* Copier les dossiers Hadoop et Spark dans les dossier MASTER et WORKER  
```$ cp -r hadoop-3.3.3/ MASTER/ && mv hadoop-3.3.3/ WORKER/```  
```$ cp -r spark-3.3.1-bin-hadoop3/ MASTER/ && mv spark-3.3.1-bin-hadoop3/ WORKER/```  
### Lancement du cluster
* Lancer le cluster :  
```$ docker-compose up -d```
* Vérifier que le cluster est bien lancé :  
```$ docker-compose ps```
* Se connecter au master :  
```$ docker exec -it master bash```
* S'assurer que le cluster est bien lancé :  
```$ jps```
* Accéder à l'interface web de Spark : http://172.20.0.2:8080
### Fichier et script de test
* L'application utilisée pour les tests est un script pySpark qui compte le nombre d'occurrences de chaque caractère dans un fichier texte.
* Le fichier texte utilisé est généré aléatoirement par le script ressources/generator_big_file.sh:  
exemple pour générer un fichier d'environ 1Go : ```$ ./ressources/generator_big_file.sh 1000000000```  
* Pour lancer le script pySpark, utiliser le script run.sh : ```$ run.sh```
* Le résultat du script est récupéré dans le dossier ```ressources/cur_output```  
## Panne d'un Datanode  
## Panne d'un Worker  
### Panne d'un worker sans travail en cours  
### Panne d'un worker avec un travail en cours  
## Panne du Namenode  
## Panne du Master  
