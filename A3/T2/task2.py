
from pyspark import SparkContext
from pyspark.sql import SQLContext

from pyspark.sql.types import FloatType
import pyspark.sql.functions as F
import sys

sc=SparkContext.getOrCreate()
sqlContext = SQLContext(sc)


city_csv = sys.argv[1]
global_csv = sys.argv[2]

city_df = sqlContext.read.option("header",True).csv(city_csv)
global_df = sqlContext.read.option("header",True).csv(global_csv)
#city_df.printSchema()

city_df = city_df.select("dt","AverageTemperature","City","Country")
global_df = global_df.select("dt","LandAverageTemperature")


city_df = city_df.withColumn("AverageTemperature",city_df.AverageTemperature.cast(FloatType()))

global_df = global_df.withColumn("LandAverageTemperature",global_df.LandAverageTemperature.cast(FloatType()))


# fill na
#city_df = city_df.na.fill({'AverageTemperature':0.0})

global_df = global_df.dropna(subset=('LandAverageTemperature'))
city_df = city_df.dropna(subset=('AverageTemperature'))

#global_df.dropna(how='all', inplace=True)
#global_df = global_df.na.fill({'LandAverageTemperature':0.0})


#city_df.show(20)
#global_df.show(20)


city_df = city_df.groupBy('dt','Country').max('AverageTemperature').orderBy('dt',ascending=False)

#city_df.show(10)

global_df = global_df.orderBy('dt',ascending=False)

df_inter = global_df.join(city_df , city_df.dt ==  global_df.dt,"inner").drop(city_df["dt"]).orderBy('dt',ascending=False)

#df_inter.show(10)


cnt_cond = lambda cond: F.sum(F.when(cond, 1).otherwise(0))

df_inter = df_inter.groupBy('Country').agg(cnt_cond( F.col('max(AverageTemperature)') > F.col('LandAverageTemperature').alias('gtr_count') )).orderBy('Country',ascending=True)
#df_inter.show(20)


rdd = df_inter.rdd

val = rdd.collectAsMap()
#print(val)

for x in val.items():
	if x[1]>0:
		print(x[0],x[1],sep='\t')
'''
val = list(map(lambda x:x.asDict(),val))

print(val)
for x in val:
	for y in x.items():
		print(y[0][0],y[1],sep='\t')
'''		

