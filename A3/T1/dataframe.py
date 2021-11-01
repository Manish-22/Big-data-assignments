from pyspark import SparkContext
from pyspark.sql import SQLContext
import sys
sc=SparkContext('local',"task1")
sqlContext = SQLContext(sc)

df = sqlContext.read.json("./inp2.json")
df.show(5)

#select => "select" in sql
df.select("author", "title", "rank", "price").show(5)

#isin => "in" in sql
df[df.author.isin("John Sandford", "Stephenie Meyer")].show(5)

df.select("author", "title", df.title.like("%THE%")).show(5) #startswith, endswith

df_del = df.drop("amazon_product_url", "published_date")
df_del.show(5)
#df_add = df.withColumn('fresh_column') #add new columns
#df_update = df.withColumnRenamed("published_date", "date") #update/rename column names

#groupBy + orderby
df_grp = df.groupBy("author").count().orderBy("count", ascending=0).show(10)
#filter
df.filter(df["title"] == "THE HOST").show(5)

#  df -> rdd
rdd1 = df.rdd
rdd1.take(5)

#  rdd -> df
df2 = rdd1.toDF()
df2.show(5)
