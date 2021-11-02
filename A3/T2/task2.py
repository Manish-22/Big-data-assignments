from pyspark import SparkContext
from pyspark.sql import SQLContext

from pyspark.sql.types import FloatType

import sys

sc=SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


city_csv = sys.argv[1]
global_csv = sys.argv[2]

city_df = sqlContext.read.option("header",True).csv(city_csv)
global_df = sqlContext.read.option("header",True).csv(global_csv)
#city_df.printSchema()

# read files

city_df = city_df.withColumn("AverageTemperature",city_df.AverageTemperature.cast(FloatType()))

city_df = city_df.drop(city_df["City"]).groupBy('dt').pivot('Country').max("AverageTemperature").orderBy('dt', ascending=False)

city_df.show(20)

#.orderBy('dt',ascending=False)
'''
#city_df = city_df.withColumn("AverageTemperature",city_df.AverageTemperature.cast(FloatType()))
'''

global_df = global_df.withColumn("LandAverageTemperature",global_df.LandAverageTemperature.cast(FloatType()))

global_df=global_df.orderBy("dt",ascending=False)

global_df.show(20)

df_inter = global_df.join(city_df , city_df.dt ==  global_df.dt,"inner").drop(city_df["dt"]).orderBy('dt',ascending=False)

df_inter.show(20)

rdd =df_inter.rdd

print(rdd.take(20))
