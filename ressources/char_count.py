from pyspark import SparkContext

def count_characters(sc, input_path, output_path):
    # Read the file into an RDD
    text_file = sc.textFile(input_path)

    # Flatten the RDD into a list of characters
    chars = text_file.flatMap(lambda line: list(line))

    # Count the occurrences of each character
    char_counts = chars.countByValue()

    # Save the character counts to a file
    # with open(output_path, "w") as f:
    #     for char, count in char_counts.items():
    #         f.write(f"{char}: {count}\n")
    char_counts_rdd = sc.parallelize([(char, count) for char, count in char_counts.items()])

    # Save the character counts to a file in HDFS
    char_counts_rdd.saveAsTextFile(output_path)

# Create a SparkContext
sc = SparkContext()
master_url = "hdfs://spark-master:54310"
# Call the word_count function
count_characters(sc, master_url + "/input/bigfile.txt", master_url + "/output/")

# Stop the SparkContext
sc.stop()