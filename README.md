# social_media_mapreduce

Steps done:

 1. Use the json_to_txt_<datagroup>.py script in the ipynb file to transform crawled JSON data to text format so its easier to insert into HDFS
 2. Use the mapper_<datagroup>.py and reducer_socmed.py for mapreducing using the corresponding txt file as input
 3. Finally, aggregate output of previous step using mapper_socmed_final.py and reducer_socmed_final.py to form a CSV file
 4. More info can also be viewed here: https://docs.google.com/document/d/1K-zqAMK6LPdPdekge6mggH8GKH4sd6E_mHi4c1ARVHk/edit?usp=sharing
 
Repositori ini dibuat untuk memenuhi tugas IF4044 MapReduce dengan data sosial media
