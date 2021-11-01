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

country_df = base_df.filter(base_df["Country"] == country)
country_df.show(5)

avg_ofavg_city = country_df.groupby("City").count()

avg_ofavg_city.show(10)

#df_grp = df.groupBy("author").count().orderBy("count", ascending=0).show(10)

aggr_avg_city = country_df
