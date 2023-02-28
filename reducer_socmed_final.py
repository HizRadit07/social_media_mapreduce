#!/home/bigdata/anaconda3/bin/python

import csv
import sys

# Define the column headers
headers = ['social_media', 'date', 'count']

# Initialize the CSV writer
csv_writer = csv.writer(sys.stdout)

# Write the headers as the first row of the output CSV file
csv_writer.writerow(headers)

# Process the input and write the output to CSV
for line in sys.stdin:
    # Split the line into key-value pairs
    socmed, date, count = line.strip().split('\t')
    # Write the key-value pair to CSV
    csv_writer.writerow([socmed, date, count])
