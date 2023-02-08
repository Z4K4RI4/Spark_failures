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
* Le fichier texte utilisé est généré aléatoirement par le script ressources/generator_big_file.sh :  
exemple pour générer un fichier d'environ 1Go : ```$ ./ressources/generator_big_file.sh 1000000000```  
* Pour lancer le script pySpark, utiliser le script run.sh : ```$ run.sh```
* Le résultat du script est récupéré dans le dossier ```ressources/cur_output```  
## Fonctionnement nominal
Le taux de réplication est fixé à 2.  
Après avoir mis le fichier bigfile.txt à l'aide de la commande ```$ hdfs dfs -put bigfile.txt /input```, 
on demande un rapport à l'aide de la commande ```$ hdfs dfsadmin -report```.
Le fichier est réparti de la façon suivante sur le cluster :  
```
root@spark-master:/home# hdfs dfsadmin -report
Configured Capacity: 2513028710400 (2.29 TB)
Present Capacity: 96757731855 (90.11 GB)
DFS Remaining: 69460893696 (64.69 GB)
DFS Used: 27296838159 (25.42 GB)
DFS Used%: 28.21%
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
DFS Used: 13648368460 (12.71 GB)
Non DFS Used: 449458965684 (418.59 GB)
DFS Remaining: 13892169728 (12.94 GB)
DFS Used%: 2.72%
DFS Remaining%: 2.76%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 18:20:20 GMT 2023
Last Block Report: Mon Feb 06 18:01:49 GMT 2023
Num of Blocks: 124


Name: 172.20.0.3:9866 (172.20.0.3)
Hostname: spark-worker1
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 3652444819 (3.40 GB)
Non DFS Used: 459454844269 (427.90 GB)
DFS Remaining: 13892214784 (12.94 GB)
DFS Used%: 0.73%
DFS Remaining%: 2.76%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 18:19:17 GMT 2023
Last Block Report: Mon Feb 06 18:01:49 GMT 2023
Num of Blocks: 44


Name: 172.20.0.4:9866 (spark-worker2.00_miniprojet_spark-network)
Hostname: spark-worker2
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 3096949798 (2.88 GB)
Non DFS Used: 460010384346 (428.42 GB)
DFS Remaining: 13892169728 (12.94 GB)
DFS Used%: 0.62%
DFS Remaining%: 2.76%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 18:20:20 GMT 2023
Last Block Report: Mon Feb 06 18:01:49 GMT 2023
Num of Blocks: 50


Name: 172.20.0.5:9866 (spark-worker3.00_miniprojet_spark-network)
Hostname: spark-worker3
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 3246625955 (3.02 GB)
Non DFS Used: 459860708189 (428.28 GB)
DFS Remaining: 13892169728 (12.94 GB)
DFS Used%: 0.65%
DFS Remaining%: 2.76%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 18:20:20 GMT 2023
Last Block Report: Mon Feb 06 18:01:49 GMT 2023
Num of Blocks: 55


Name: 172.20.0.6:9866 (spark-worker0.00_miniprojet_spark-network)
Hostname: spark-worker0
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 3652449127 (3.40 GB)
Non DFS Used: 459454885017 (427.90 GB)
DFS Remaining: 13892169728 (12.94 GB)
DFS Used%: 0.73%
DFS Remaining%: 2.76%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 18:20:20 GMT 2023
Last Block Report: Mon Feb 06 18:01:49 GMT 2023
Num of Blocks: 49
```  
La commande `hdfs fsck hdfs://spark-master:54310/input/bigfile.txt` renvoie : 
```
root@spark-master:/home# hdfs fsck hdfs://spark-master:54310/input/bigfile.txt
Connecting to namenode via http://spark-master:9870/fsck?ugi=root&path=%2Finput%2Fbigfile.txt
FSCK started by root (auth:SIMPLE) from /172.20.0.2 for path /input/bigfile.txt at Tue Feb 07 14:52:29 GMT 2023


Status: HEALTHY
 Number of data-nodes:	5
 Number of racks:		1
 Total dirs:			0
 Total symlinks:		0

Replicated Blocks:
 Total size:	13541700000 B
 Total files:	1
 Total blocks (validated):	101 (avg. block size 134076237 B)
 Minimally replicated blocks:	101 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	2
 Average block replication:	2.0
 Missing blocks:		0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)
 Blocks queued for replication:	0

Erasure Coded Block Groups:
 Total size:	0 B
 Total files:	0
 Total block groups (validated):	0
 Minimally erasure-coded block groups:	0
 Over-erasure-coded block groups:	0
 Under-erasure-coded block groups:	0
 Unsatisfactory placement block groups:	0
 Average block group size:	0.0
 Missing block groups:		0
 Corrupt block groups:		0
 Missing internal blocks:	0
 Blocks queued for replication:	0
FSCK ended at Tue Feb 07 14:52:29 GMT 2023 in 19 milliseconds


The filesystem under path '/input/bigfile.txt' is HEALTHY
```
Le script char_count.py est lancé avec la commande  
```$ spark-submit --master spark://spark-master:7077 /ressources/char_count.py```.
Le résultat est sauvegardé dans le dossier `ressources/outputTrue`.
# Scénarios de panne
## Panne d'un Datanode  
Le caintainer `spark-worker1` est arrêté avec la commande ```$ docker compose stop spark-worker1```.
Les commandes ```$ hdfs dfsadmin -report``` et ```hdfs fsck hdfs://spark-master:54310/input/bigfile.txt``` donnent les mêmes résultats qu'initialement. Le datanode associé au spark-worker1 est toujours présent dans le rapport.  
Après l'arrêt du datanode, le script est relancé. Le résultat est sauvegardé dans le dossier `ressources/outputDatanodeDown`.  
Le résultat est le même que précédemment. La réplication des données a fonctionné normalement.  
## Panne d'un Spark Worker
### Panne d'un worker sans travail en cours  
Le caintainer `spark-worker1` est arrêté avec la commande ```$ docker compose stop spark-worker1```.
La commande ```$ hdfs dfsadmin -report``` donne le même résultat qu'initialement. Le datanode associé au spark-worker1 est toujours présent dans le rapport.
Le script est relancé après l'arrêt du worker. Le résultat est sauvegardé dans le dossier `ressources/outputWorkerDown`.  
Le résultat est le même que précédemment. Spark a fonctionné normalement avec un Worker en moins.  
### Panne d'un worker avec un travail en cours  
Le caintainer `spark-worker2` est arrêté avec la commande ```$ docker compose stop spark-worker2```, après avoir lancé le script `char_count.py`.  
La panne apparait dans la sortie de Spark, au travers d'un "WARN TransportChannelHandler"' :  
```
23/02/06 18:36:40 WARN TransportChannelHandler: Exception in connection from /172.20.0.4:36136
java.io.IOException: Connection reset by peer
	at java.base/sun.nio.ch.FileDispatcherImpl.read0(Native Method)
	at java.base/sun.nio.ch.SocketDispatcher.read(SocketDispatcher.java:39)
	at java.base/sun.nio.ch.IOUtil.readIntoNativeBuffer(IOUtil.java:276)
	at java.base/sun.nio.ch.IOUtil.read(IOUtil.java:233)
	at java.base/sun.nio.ch.IOUtil.read(IOUtil.java:223)
	at java.base/sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:356)
	at io.netty.buffer.PooledByteBuf.setBytes(PooledByteBuf.java:258)
	at io.netty.buffer.AbstractByteBuf.writeBytes(AbstractByteBuf.java:1132)
	at io.netty.channel.socket.nio.NioSocketChannel.doReadBytes(NioSocketChannel.java:350)
	at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:151)
	at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:722)
	at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:658)
	at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:584)
	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:496)
	at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:986)
	at io.netty.util.internal.ThreadExecutorMap$2.run(ThreadExecutorMap.java:74)
	at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30)
	at java.base/java.lang.Thread.run(Thread.java:829)
23/02/06 18:36:40 ERROR TaskSchedulerImpl: Lost executor 0 on 172.20.0.4: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 8.0 in stage 0.0 (TID 8) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 11.0 in stage 0.0 (TID 11) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 14.0 in stage 0.0 (TID 14) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 13.0 in stage 0.0 (TID 13) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 10.0 in stage 0.0 (TID 10) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 9.0 in stage 0.0 (TID 9) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 12.0 in stage 0.0 (TID 12) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 WARN TaskSetManager: Lost task 15.0 in stage 0.0 (TID 15) (172.20.0.4 executor 0): ExecutorLostFailure (executor 0 exited caused by one of the running tasks) Reason: worker lost
23/02/06 18:36:40 INFO TaskSchedulerImpl: Handle removed worker worker-20230206180210-172.20.0.4-35855: 172.20.0.4:35855 got disassociated
23/02/06 18:36:40 INFO DAGScheduler: Executor lost: 0 (epoch 0)
23/02/06 18:36:40 INFO BlockManagerMasterEndpoint: Trying to remove executor 0 from BlockManagerMaster.
23/02/06 18:36:40 INFO BlockManagerMasterEndpoint: Removing block manager BlockManagerId(0, 172.20.0.4, 35873, None)
23/02/06 18:36:40 INFO BlockManagerMaster: Removed 0 successfully in removeExecutor
```
Le résultat est sauvegardé dans le dossier `ressources/outputWorkerDownWithJob`.  
Le résultat est le même que précédemment. Spark a fonctionné normalement avec un Worker en moins.  
Spark a pu continuer à fonctionner avec un Worker en moins, car il a pu répartir les tâches sur les Workers restants.  
## Panne du Namenode  
Le processus du Namenode est arrêté depuis le container `spark-master`.
Il s'agit ici du processus 246 :  
```
root@spark-master:/home# jps
854 Worker
4470 Jps
246 NameNode
745 Master
589 SecondaryNameNode
```
Il est alors impossible de lancer le script :  
```
py4j.protocol.Py4JJavaError: An error occurred while calling z:org.apache.spark.api.python.PythonRDD.collectAndServe.
: java.net.ConnectException: Call From spark-master/172.20.0.2 to spark-master:54310 failed on connection exception: java.net.ConnectException: Connection refused; For more details see:  http://wiki.apache.org/hadoop/ConnectionRefused
```
Après avoir relancer le namenode, le rapport est le suivant : 
```
root@spark-master:/home# hdfs dfsadmin -report
Configured Capacity: 1507817226240 (1.37 TB)
Present Capacity: 45941216598 (42.79 GB)
DFS Remaining: 18644025344 (17.36 GB)
DFS Used: 27297191254 (25.42 GB)
DFS Used%: 59.42%
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
Live datanodes (3):

Name: 172.20.0.2:9866 (spark-master)
Hostname: spark-master
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 13648562859 (12.71 GB)
Non DFS Used: 457136244053 (425.74 GB)
DFS Remaining: 6214696960 (5.79 GB)
DFS Used%: 2.72%
DFS Remaining%: 1.24%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 19:18:48 GMT 2023
Last Block Report: Mon Feb 06 19:18:18 GMT 2023
Num of Blocks: 101


Name: 172.20.0.5:9866 (spark-worker3.00_miniprojet_spark-network)
Hostname: spark-worker3
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 6749555371 (6.29 GB)
Non DFS Used: 464035284309 (432.17 GB)
DFS Remaining: 6214664192 (5.79 GB)
DFS Used%: 1.34%
DFS Remaining%: 1.24%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 19:18:50 GMT 2023
Last Block Report: Mon Feb 06 19:18:20 GMT 2023
Num of Blocks: 50


Name: 172.20.0.6:9866 (spark-worker0.00_miniprojet_spark-network)
Hostname: spark-worker0
Decommission Status : Normal
Configured Capacity: 502605742080 (468.09 GB)
DFS Used: 6899073024 (6.43 GB)
Non DFS Used: 463885766656 (432.03 GB)
DFS Remaining: 6214664192 (5.79 GB)
DFS Used%: 1.37%
DFS Remaining%: 1.24%
Configured Cache Capacity: 0 (0 B)
Cache Used: 0 (0 B)
Cache Remaining: 0 (0 B)
Cache Used%: 100.00%
Cache Remaining%: 0.00%
Xceivers: 0
Last contact: Mon Feb 06 19:18:50 GMT 2023
Last Block Report: Mon Feb 06 19:18:20 GMT 2023
Num of Blocks: 51
```
Le script est relancé, les résultats sont sauvegardés dans le dossier `ressources/outputNamenodeDown`.
Le résultat est le même que précédemment. Le Namenode a bien repris son fonctionnement après avoir été relancé.