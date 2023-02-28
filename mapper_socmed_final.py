#!/home/bigdata/anaconda3/bin/python
#mapper

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	social_media, date, count = data
	
	print("%s\t%s\t%s" % (social_media, date, count))
	
	
