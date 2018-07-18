import csv
column = []
with open('AQI_20180717093049.csv','r',encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    column = [row[0]for row in reader]
with open('AQI_20180717093049.csv','r',encoding = 'utf-8-sig') as f:
    reader = csv.reader(f)
    column3 = [row[2]for row in reader]
column2 = []
for i in range(1,len(column3)):
    column2.append(int(column3[i]))
site = column[1]
AQI = column2[1]
for i in range(0, len(column2)):
    if column2[i] < AQI:
        AQI = column2[i]
        site = column[i + 1]
print(site)
print(AQI)