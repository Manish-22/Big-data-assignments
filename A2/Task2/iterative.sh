#!/bin/sh
CONVERGE=1
ITER=1
rm v.txt v1.txt log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /Assignment-2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task1/mapper.py'" \
-reducer "'/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task1/reducer.py' '/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/v.txt'" \
-input /Assignment-2/Input/dataset-sample2.txt \
-output /Assignment-2/output/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/mapper.py' '/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/v.txt' '/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/embedding-sample2.json'" \
	-reducer "'/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/reducer.py'" \
	-input /Assignment-2/output/task-1-output/part-00000 \
	-output /Assignment-2/output/task-2-output
	touch v1.txt
	hadoop fs -cat /Assignment-2/output/task-2-output/part-00000 > "/home/pes1ug19cs599/Desktop/Big-data-assignments/A2/Task2/v1.txt"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /Assignment-2/output/task-2-output/
	echo $CONVERGE
done
