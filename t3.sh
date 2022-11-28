#!/bin/bash

for i in $(ls Carpeta_1); do
	mapred streaming -files mapper.py,reducer.py -input /user/hadoop/Carpeta_1/$i -output /output/$i -mapper ./mapper.py -reducer ./reducer.py
done

for i in $(ls Carpeta_2); do
        mapred streaming -files mapper.py,reducer.py -input /user/hadoop/Carpeta_2/$i -output /output/$i -mapper ./mapper.py -reducer ./reducer.py
done

clear

hdfs dfs -get /output/* Outputs

python3 format.py

python3 bd_upload.py



