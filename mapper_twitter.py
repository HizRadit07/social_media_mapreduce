#!/home/bigdata/anaconda3/bin/python
#mapper

import sys
import json
from datetime import datetime


for line in sys.stdin:
	data = line.strip()
	jsondata = json.loads(data)
	
	for i in jsondata:
		curdate = datetime.strftime(datetime.strptime(i['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
		print("%s\t%s\t%s" % ('twitter', curdate, 1))
