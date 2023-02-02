import numpy as np
from pyspark.ml.linalg import DenseMatrix
from pyspark.sql.functions import col
from pyspark.sql.types import Row
from pyspark.sql import SparkSession
from pyspark.ml.linalg import DenseMatrix, CholeskyDecomposition
master_url = "hdfs://spark-master:54310"
spark = SparkSession.builder.appName("LU Factorization").getOrCreate()

# matrix_rdd = spark.sparkContext.binaryFiles(f"{master_url}/input/matrix.npy").map(
#     lambda x: np.frombuffer(x[1], dtype=np.float64))
matrix_rdd = spark.sparkContext.binaryFiles(f"{master_url}/input/matrix.npy").map(
    # lambda x: np.load(x[1], allow_pickle=True)).flatMap(lambda x: x)
    lambda x: x[1]).flatMap(lambda x: x)


# Create Dataframe
matrix_df = spark.createDataFrame(matrix_rdd.map(lambda x: Row(x)))

# Compute LU Factorization
# lu_matrix = DenseMatrix(1000, 1000, matrix_rdd.collect())
matrix_data = matrix_rdd.take(1000 * 1000)
# distributed LU factorization :
lu_matrix = DenseMatrix(1000, 1000, matrix_data)
cholesky = CholeskyDecomposition(lu_matrix)

# Saving the result in hdfs
cholesky.L.toArray().toDF().write.mode("overwrite").parquet(f"{master_url}/output/L.parquet")
cholesky.U.toArray().toDF().write.mode("overwrite").parquet(f"{master_url}/output/U.parquet")


# lu_matrix = DenseMatrix(1000, 1000, matrix_data)
# lu = lu_matrix.tallSkinnyLU(True)

# Saving the result in hdfs
# lu.L.toArray().toDF().write.mode("overwrite").parquet(f"{master_url}/output/L.parquet")
# lu.U.toArray().toDF().write.mode("overwrite").parquet(f"{master_url}/output/U.parquet")


def check_result(L_path, U_path, matrix_path):
    matrix_rdd = spark.sparkContext.binaryFiles(f"{master_url}/input/matrix.npy").map(
        lambda x: np.load(x[1], allow_pickle=True)).flatMap(lambda x: x)

    matrix = DenseMatrix(1000, 1000, matrix_rdd.collect())

    # Load the L and U matrices from HDFS
    L = spark.read.parquet(L_path).collect()
    U = spark.read.parquet(U_path).collect()
    L_matrix = np.array([x[0] for x in L])
    U_matrix = np.array([x[0] for x in U])

    # Compute L*U
    LU = np.dot(L_matrix, U_matrix)

    # Check if L*U is equal to the original matrix
    is_equal = np.allclose(LU, matrix.toArray(), rtol=1e-05, atol=1e-08)
    if is_equal:
        print("\033[92m" + "Result is correct" + "\033[0m")
        return True
    else:
        errors = np.count_nonzero(LU - matrix.toArray())
        print("\033[91m" + "Result is incorrect" + "\033[0m")
        print(f"Number of errors: {errors}")
        return False

#Check the result is correct
A = np.load(f"{master_url}/input/matrix.npy")
L = np.load(f"{master_url}/output/L.parquet")
U = np.load(f"{master_url}/output/U.parquet")
result = np.dot(L,U)
errors = np.count_nonzero(A - result)

if errors == 0:
    spark.sparkContext.parallelize(["Factorization is correct"]).saveAsTextFile(f"{master_url}/result")
else:
    spark.sparkContext.parallelize([f"Number of errors: {errors}"]).saveAsTextFile(f"{master_url}/result")
