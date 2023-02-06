wget "https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz" && tar -xvf hadoop-3.3.3.tar.gz && rm hadoop-3.3.3.tar.gz
wget "https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz" && tar -xvf spark-3.3.1-bin-hadoop3.tgz && rm spark-3.3.1-bin-hadoop3.tgz
cp ressources/configurations_files/hadoop/* hadoop-3.3.3/etc/hadoop/
cp ressources/configurations_files/spark/* spark-3.3.1-bin-hadoop3/conf/
cp -r hadoop-3.3.3/ MASTER/ && mv hadoop-3.3.3/ WORKER/
cp -r spark-3.3.1-bin-hadoop3/ MASTER/ && mv spark-3.3.1-bin-hadoop3/ WORKER/