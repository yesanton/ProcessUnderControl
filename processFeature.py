'''

Time between event 'A_PARTLYSUBMITTED' and 'W_Completeren aanvraag'
should be less than 7 hours

for a maonth from 2012/02/01 to 2012/03/01
'''
import time

from ImportData import importData

data = importData()

dataRange = (time.strptime("2012/02/01", "%Y/%m/%d"),time.strptime("2012/03/01", "%Y/%m/%d"))
dataRange = (time.strptime("2012/01/01", "%Y/%m/%d"),time.strptime("2012/02/01", "%Y/%m/%d"))


data_in_range = []

for d in data:
    if dataRange[0] <= d[3] <= dataRange[1]:
        data_in_range.append(d)

di = dict()

for d in data_in_range:
    if d[7] == 'A_PARTLYSUBMITTED' or d[7] == 'W_Completeren aanvraag':
        if not d[0] in di:
            di[d[0]] = list()
            di[d[0]].append((d[7], d[3]))
        else:
            di[d[0]].append((d[7], d[3]))


d1 = None
d0 = None

count2 = count1 = 0

for i in di:
    for j in di[i]:
        if j[0] == 'A_PARTLYSUBMITTED':
           d0 = j[1]
        elif j[0] == 'W_Completeren aanvraag':
            d1 = j[1]

    if d1 and d0:
        time_diff = (time.mktime(d1) - time.mktime(d0)) / (60 * 60)
        count1 += 1
        if time_diff < 7: #hours
            count2 += 1
        print ('duration: ' + str(time_diff))
    d1 = None
    d0 = None


print ("Number of satissfying constrains: " + str(count2/float(count1)))


















