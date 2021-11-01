from pyspark import SparkContext
from pyspark.sql import SQLContext

from pyspark.sql.types import FloatType

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
#base_df.show(20)

base_df.drop('dt')
#base_df = base_df.withColumn("AverageTemperature",base_df.AverageTemperature.cast(FloatType()))

country_df = base_df.filter(base_df["Country"] == country)
country_df = country_df.withColumn("AverageTemperature",country_df.AverageTemperature.cast(FloatType())).orderBy('City',ascending=True)

#country_df.show(5)

#count_ofavg_city = country_df.groupby("City").count()

#count_ofavg_city.show(10)

#df_grp = df.groupBy("author").count().orderBy("count", ascending=0).show(10)

#country_df.AverageTemperature = country_df.AverageTemperature.cast(FloatType())

avg_ofavg_city = country_df.groupBy("City").avg("AverageTemperature")
#avg_ofavg_city.show(10)


df_inter = country_df.join(avg_ofavg_city , country_df.City ==  country_df.City,"inner").drop(country_df["City"]).orderBy('City',ascending=True)
#df_inter.show()


df_filtered = df_inter.filter(df_inter.AverageTemperature > df_inter['avg(AverageTemperature)'])
#df_filtered.show()

#df_filetered = df_filtered.groupBy("City").count() 
#df_filetered = df_filtered.select("City") 
#df_filtered.show()


rdd = df_filtered.rdd
#print(rdd.take(10))
rdd = rdd.map(lambda x:x['City'])
#rdd = rdd.collect()

rdd = rdd.countByValue()

#print(rdd.take(100))

for x in rdd.items():
	print(x[0],x[1],sep='\t')

