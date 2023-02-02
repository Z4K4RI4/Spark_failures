import argparse
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=1000)
parser.add_argument('--namenode', type=str, default='spark-master')
parser.add_argument('--port', type=int, default=54310)
args = parser.parse_args()

namenode = args.namenode
n = args.n
port = args.port


def generate_matrix(size):
    A = np.random.rand(size, size)
    return np.dot(A, A.T)


def write_matrix_to_hdfs(matrix, path):
    spark = SparkSession.builder.appName("Write Matrix to HDFS").getOrCreate()
    sc = spark.sparkContext
    matrix_rdd = sc.parallelize(matrix)
    # matrix_rdd.saveAsTextFile(path)
    # Convert matrix to RDD
    # Save RDD to HDFS
    matrix_rdd.saveAsTextFile(f"hdfs://{namenode}:{port}/input/matrix.npy")


# n = 1000
path = "/input/matrix.npy"

matrix = generate_matrix(n)
write_matrix_to_hdfs(matrix, path)

# client = InsecureClient(f'http://{namenode}:{port}')
# with client.write('/input/matrix.npy', encoding='utf-8') as writer:
#     np.save(writer, generate_matrix(n))
