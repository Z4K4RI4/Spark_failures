hdfs dfs -rm /output/*
hdfs dfs -rmdir /output
hdfs dfs -put /ressources/bigfile.txt /input
spark-submit --master spark://spark-master:7077 /ressources/char_count.py

hdfs dfs -get hdfs://spark-master:54310/output /ressources/cur_output
