#!/home/bigdata/anaconda3/bin/python
#mapper

import sys
import json
from datetime import datetime


for line in sys.stdin:
	data = line.strip()
	jsondata = json.loads(data)
	
	for i in jsondata:
    		cur_date = i['created_time'][:10]
    		print("%s\t%s\t%s" % ('facebook', cur_date, 1))
    		for item in i['comments']['data']:
        		cur_date = item['created_time'][:10]
        		print("%s\t%s\t%s" % ('facebook', cur_date, 1))
