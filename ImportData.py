'''
This file to be used as a import for the logs


Author: Anton Yeshchenko
'''
import csv
import time

date_fields = [50,59,85,86,110,121,122]
eventlog = "HospitalLog.csv"






csvfile = open('Data/%s' % eventlog, 'r')


logreader = csv.reader(csvfile, delimiter=';', quotechar='|')
header = next(logreader, None)  # skip the headers



activities = []

for row in logreader:
    row_temp = row
    for i in date_fields:
        row_temp[i] = time.strptime(row_temp[i], "%Y-%m-%d %H:%M:%S")
    activities.append(row)



