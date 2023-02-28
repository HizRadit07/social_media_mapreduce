#!/home/bigdata/anaconda3/bin/python
#mapper

import sys
import json
from datetime import datetime


for line in sys.stdin:
	data = line.strip()
	jsondata = json.loads(data)
	
	for i in jsondata:
		cur_date = datetime.utcfromtimestamp(int(i['created_time'])).strftime('%Y-%m-%d')
		print("%s\t%s\t%s" % ('instagram', cur_date, 1))
