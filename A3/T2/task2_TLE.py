from pyspark import SparkContext
from pyspark.sql import SQLContext

from pyspark.sql.types import FloatType
from pyspark.sql.functions import *
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
global_df = global_df.dropna(subset=('LandAverageTemperature'))
city_df = city_df.dropna(subset=('AverageTemperature'))


# read files

city_df = city_df.drop(city_df["City"]).groupBy('dt').pivot('Country')

#city_df.count().show()

city_df=city_df.max("AverageTemperature").orderBy('dt', ascending=False)		# lexico col wise
#city_df.show(20)

#city_df = city_df.na.fill(value=0.0)		# in case that country doesn't have reading for that day
#city_df.show(20)

#.orderBy('dt',ascending=False)
'''
#city_df = city_df.withColumn("AverageTemperature",city_df.AverageTemperature.cast(FloatType()))
'''



global_df=global_df.orderBy("dt",ascending=False)

#global_df.show(20)


df_inter = global_df.join(city_df , city_df.dt ==  global_df.dt,"inner").drop(city_df["dt"]).orderBy('dt',ascending=False)

#df_inter.show(20)

num_countries = len(df_inter.columns)-2		# only col of countries

for i in range(num_countries):
	df_inter = df_inter.withColumn(df_inter.columns[i+2],when( (df_inter.LandAverageTemperature < df_inter[df_inter.columns[i+2]]) & (df_inter[df_inter.columns[i+2]].isNotNull()) , 1).otherwise(0)).drop(df_inter[df_inter.columns[i+2]])
	#final.show(20)
	
cols = ("LandAverageTemperature","dt")
df_inter = df_inter.drop(*cols)

#df_inter.show(20)


final = df_inter.groupBy().sum().collect()[0]

final = final.asDict()
#print(final)

for x in final.items():
	if x[1]>0:
		print(x[0][4:-1],x[1],sep='\t') 

'''
for i in vals:
	print(i)
'''


#num_col = len(df

#final = df_inter.withColumn('Germany',when(df_inter.LandAverageTemperature < df_inter.Germany, 1).otherwise(0)).drop(df_inter['Germany'])


#final.show(20)

#print(final.groupBy().sum().collect())
