#!/home/bigdata/anaconda3/bin/python
#mapper

import sys
import json
from datetime import datetime


for line in sys.stdin:
	data = line.strip()
	jsondata = json.loads(data)
	
	for i in jsondata:
		if 'publishedAt' in i['snippet'].keys():
			curdate = i['snippet']['publishedAt'][:10]
			print("%s\t%s\t%s" % ('youtube', curdate, 1))
