from pyspark import SparkContext
import sys


#country = sys.argv[0]
#path = sys.argv[1]

sc=SparkContext('local',"task1")


text_file = sc.textFile('./Desktop/assn_3/city_sample.csv')

rdd = text_file.map(lambda line:line.split(','))

header = rdd.first()
rdd = rdd.filter(lambda x:x!=header)

#rdd = rdd.filter(lambda x:x if(country in x) else None)

rdd = rdd.map(lambda x:(x[2],x[1]))

#rdd.take(20)



rdd1 = rdd.reduceByKey(lambda x,y:int(x)+int(y))		# aggr
rdd1.take(20)

rdd2 = rdd.combineByKey( (lambda x:(x,1)) , (lambda x,y:( int(x[0])+int(y),int(x[1])+1) ) , (lambda x,y: ( int(x[0]) + int(y[0]), int(x[1]) + int(y[1]))) )
rdd2.take(20)								# key-wise aggr,count

rdd3 = rdd2.mapValues(lambda x:int(x[0])/int(x[1]))
rdd3.take(20)						# key -> avg val


rdd_n = rdd.groupByKey()
rdd_n = rdd_n.mapValues(lambda x:list(x))
rdd_n.take(20)						# key -> [list of vals]


rdd5 = rdd_n.join(rdd3)
rdd5.take(20)

def count(x):
	i=0
	for j in x[0]:
		if int(j)>int(x[1]):
			i+=1
	return i
	
rdd6 = rdd5.mapValues(count)
rdd6.take(20)

print("RESULT\n:",rdd6.take(20))

rdd6.saveAsTextFile("./t1_op")
