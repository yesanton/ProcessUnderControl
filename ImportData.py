'''
This file to be used as a import for the logs


Author: Anton Yeshchenko
'''
import csv
import time

date_fields = [50,59,85,86,110,121,122]
eventlog = "Hospital Log.csv"






csvfile = open('Data/%s' % eventlog, 'r')


logreader = csv.reader(csvfile, delimiter=';', quotechar='|')
header = next(logreader, None)  # skip the headers



activities = []

for row in logreader:
    row_temp = row
    for i in date_fields:
        data_temp = row_temp[i][:19]
        if not data_temp == "":
            row_temp[i] = time.strptime(data_temp, "%Y-%m-%dT%H:%M:%S")  #"%Y-%m-%d %H:%M:%S")
    activities.append(row)

print ("Hello, here we inported files")


