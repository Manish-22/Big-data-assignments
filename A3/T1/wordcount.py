from pyspark import SparkContext
import sys


sc=SparkContext('local',"task1")


text_file = sc.textFile("./inp1.txt") #will be reading from hdfs in the beginning


print(text_file.take(100))
rdd1_flatmap = text_file.flatMap(lambda line: line.split(" ")) #transformation
print(rdd1_flatmap)
print("flatmap():\t", rdd1_flatmap.take(5))


rdd2_map = rdd1_flatmap.map(lambda word: (word, 1)) #transformation
print("map():\t\t", rdd2_map.take(5))


counts = rdd2_map.reduceByKey(lambda a, b: a + b) #action - rdd created here
print("reduceByKey():\t", counts.take(10))


counts.saveAsTextFile("./op1")
