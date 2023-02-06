FROM ubuntu
RUN apt-get update
RUN apt-get install -y locales openjdk-11-jdk scala git wget curl python3 ssh python3-pip
RUN rm -rf /var/lib/apt/lists/*
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
#RUN pip3 install numpy
#RUN pip3 install hdfs
ENV LANG en_US.utf8
WORKDIR /home
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:JAVA_HOME/bin
# installing hadoop
#RUN wget -O hadoop.tar.gz "https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz"
#RUN tar -xf hadoop.tar.gz
COPY hadoop-3.3.3 hadoop-3.3.3
RUN mv hadoop-3.3.3 /opt/hadoop
ENV HADOOP_HOME=/opt/hadoop/
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
# installing spark
#RUN wget -O spark.tgz "https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz"
#RUN tar -xf spark.tgz
#RUN rm spark.tgz
COPY spark-3.3.1-bin-hadoop3 spark-3.3.1-bin-hadoop3
RUN mv spark-3.3.1-bin-hadoop3 /opt/spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PATH=$PATH:/ressources/scripts
# ssh configuration
COPY ssh/id_rsa /root/.ssh/id_rsa
COPY ssh/authorized_keys /root/.ssh/authorized_keys
RUN bash -c "eval "$(ssh-agent -s)" && ssh-add /root/.ssh/id_rsa"
#ENTRYPOINT bash -c "start-master.sh && tail -f /dev/null"
ENTRYPOINT bash -c "service ssh start && tail -f /dev/null"
#        && hdfs namenode -format && start-dfs.sh && hdfs dfs -mkdir /input && start-master.sh \
EXPOSE 8080
