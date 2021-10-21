import csv
import numpy as np
#reading the file
filename='C:/Users/1/Desktop/bungeetech/input/question-3/main.csv'
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

#getting team and card indexes
for i in range(len(fields)):
    if fields[i]=='Team':
        teamindex=i
    elif fields[i]=='Yellow Cards':
        yindex=i
    elif fields[i] == 'Red Cards':
        rindex = i

teams=[]
for row in rows:
    if row[teamindex] not in teams:
        teams.append([row[teamindex],int(row[yindex]),int(row[rindex])])
    else:
        continue

teams=np.array(teams)
newteams= teams[np.argsort(teams[:, 1])]
teams= newteams[np.argsort(newteams[:, 2])]

teams=np.flipud(teams)
#making the csv file
f = open('C:/Users/1/Desktop/bungeetech/output/answer-3/answer.csv', 'w')
writer = csv.writer(f)
fields=['team','yellow cards','red cards']
writer.writerow(fields)
for row in teams:
    writer.writerow(row)
f.close()
