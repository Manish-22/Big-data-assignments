from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys
sc=SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


country = sys.argv[1]
path = sys.argv[2]


text_file = sc.textFile(path)


rdd = text_file.map(lambda line:line.split(','))

header = rdd.first()

rdd = rdd.filter(lambda x:x!=header)

base_df = rdd.toDF(header)
base_df.show(20)


