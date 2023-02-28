#!/home/bigdata/anaconda3/bin/python
#mapper

import sys
import json
from datetime import datetime

datasrc = ['anaktester_go','byu.id','gridoto_news','myxl','telkomsel']
linecount = 0

for line in sys.stdin:
	data = line.strip()
	jsondata = json.loads(data)
	
	for i in jsondata["GraphImages"]:
		if('taken_at_timestamp' in i.keys()):
			curdate = datetime.utcfromtimestamp(i['taken_at_timestamp']).strftime('%Y-%m-%d')
			print("%s\t%s\t%s" % (datasrc[linecount], curdate, 1))
		if('comments' in i.keys()):
			for item in i['comments']['data']:
				curdate = datetime.utcfromtimestamp(item['created_at']).strftime('%Y-%m-%d')
				print("%s\t%s\t%s" % (datasrc[linecount], curdate, 1))
	
	linecount += 1
