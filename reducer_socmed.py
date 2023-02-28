#!/home/bigdata/anaconda3/bin/python
#reducer

import sys

old_key = None
count = 0

for line in sys.stdin:
	# 'asdf'	'tgl'	1
	data = line.strip().split("\t")
	
	cur_socmed, cur_date, cur_count = data
	cur_key = (cur_socmed, cur_date)

	if (old_key and old_key != cur_key):
		print("%s\t%s\t%s" % (old_key[0], old_key[1], count))
		count = 0
	
	old_key = cur_key
	count += int(cur_count)

if (old_key != None):
	print("%s\t%s\t%s" % (old_key[0], old_key[1], count))
		
