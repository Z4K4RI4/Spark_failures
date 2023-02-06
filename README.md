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
```$ docker-compose exec -it master bash```
* S'assurer que le cluster est bien lancé :  
```$ jps```
* Accéder à l'interface web de Spark : http://172.20.0.2:8080
### Fichier et script de test
* L'application utilisée pour les tests est un script pySpark qui compte le nombre d'occurrences de chaque caractère dans un fichier texte.
* Le fichier texte utilisé est généré aléatoirement par le script ressources/generator_big_file.sh:  
exemple pour générer un fichier d'environ 1Go : ```$ ./ressources/generator_big_file.sh 1000000000```  
* Pour lancer le script pySpark, utiliser le script run.sh : ```$ run.sh```
* Le résultat du script est récupéré dans le dossier ```ressources/cur_output```  
## Fonctionnement nominal
Après avoir mis le fichier bigfile.txt à l'aide de la commande ```$ hdfs dfs -put bigfile.txt /input```, 
on demande un rapport à l'aide de la commande ```$ hdfs dfsadmin -report```.
Le fichier est réparti de la façon suivante sur le cluster :  
```
root@spark-master:/home# hdfs dfsadmin -report
Configured Capacity: 2513028710400 (2.29 TB)
Present Capacity: 69755709769 (64.97 GB)
DFS Remaining: 28643143680 (26.68 GB)
DFS Used: 41112566089 (38.29 GB)
DFS Used%: 58.94%
Replicated Blocks:
	Under replicated blocks: 0
	Blocks with corrupt replicas: 0
	Missing blocks: 0
	Missing blocks (with replication factor 1): 0
	Low redundancy blocks with highest priority to recover: 0
	Pending deletion blocks: 0
Erasure Coded Block Groups:
	Low redundancy block groups: 0
	Block groups with corrupt internal blocks: 0
	Missing block groups: 0
	Low redundancy blocks with highest priority to recover: 0
	Pending deletion blocks: 0

-------------------------------------------------
Live datanodes (5):

Name: 172.20.0.2:9866 (spark-master)
Hostname: spark-master
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 13678255513 (12.74 GB)
Non DFS Used: 457592619623 (426.17 GB)
DFS Remaining: 5728628736 (5.34 GB)
DFS Used%: 2.72%
DFS Remaining%: 1.14%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 10:30:08 GMT 2023
Last Block Report: Mon Feb 06 10:19:17 GMT 2023
Num of Blocks: 101


Name: 172.20.0.3:9866 (spark-worker0.00_miniprojet_spark-network)
Hostname: spark-worker0
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 6087385088 (5.67 GB)
Non DFS Used: 465183490048 (433.24 GB)
DFS Remaining: 5728628736 (5.34 GB)
DFS Used%: 1.21%
DFS Remaining%: 1.14%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 10:30:07 GMT 2023
Last Block Report: Mon Feb 06 10:19:16 GMT 2023
Num of Blocks: 45


Name: 172.20.0.4:9866 (spark-worker2.00_miniprojet_spark-network)
Hostname: spark-worker2
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 5855293475 (5.45 GB)
Non DFS Used: 465415581661 (433.45 GB)
DFS Remaining: 5728628736 (5.34 GB)
DFS Used%: 1.16%
DFS Remaining%: 1.14%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 10:30:07 GMT 2023
Last Block Report: Mon Feb 06 10:19:16 GMT 2023
Num of Blocks: 43


Name: 172.20.0.5:9866 (spark-worker3.00_miniprojet_spark-network)
Hostname: spark-worker3
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 7228644810 (6.73 GB)
Non DFS Used: 464042230326 (432.17 GB)
DFS Remaining: 5728628736 (5.34 GB)
DFS Used%: 1.44%
DFS Remaining%: 1.14%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 10:30:07 GMT 2023
Last Block Report: Mon Feb 06 10:19:16 GMT 2023
Num of Blocks: 53


Name: 172.20.0.6:9866 (spark-worker1.00_miniprojet_spark-network)
Hostname: spark-worker1
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 8262987203 (7.70 GB)
Non DFS Used: 463007887933 (431.21 GB)
DFS Remaining: 5728628736 (5.34 GB)
DFS Used%: 1.64%
DFS Remaining%: 1.14%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 10:30:07 GMT 2023
Last Block Report: Mon Feb 06 10:19:16 GMT 2023
Num of Blocks: 61
```  

Le script char_count.py est lancé avec la commande  
```$ spark-submit --master spark://spark-master:7077 /ressources/char_count.py```.
## Scénarios de panne
## Panne d'un Datanode 
## Panne d'un Worker  
### Panne d'un worker sans travail en cours  
### Panne d'un worker avec un travail en cours  
## Panne du Namenode  
## Panne du Master  
