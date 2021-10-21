
import csv
#reading the file
filename='C:/Users/1/Desktop/bungeetech/input/question-2/main.csv'
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

#getting age and occupation index
for i in range(len(fields)):
    if fields[i]=='age':
        ageindex=i
    elif fields[i]=='occupation':
        occupationindex=i
#differentiating according to age
occupationmaxage={}
occupationminage={}
for row in rows:
    if row[occupationindex] not in occupationmaxage:
        occupationminage[row[occupationindex]]=200
        occupationmaxage[row[occupationindex]]=0
    if int(row[ageindex]) >occupationmaxage[row[occupationindex]]:
        occupationmaxage[row[occupationindex]]=int(row[ageindex])
    if int(row[ageindex])<occupationminage[row[occupationindex]]:
        occupationminage[row[occupationindex]]=int(row[ageindex])

sortedkeys=sorted(occupationmaxage.keys())

#making the csv file
f = open('C:/Users/1/Desktop/bungeetech/output/answer-2/answer.csv', 'w')
writer = csv.writer(f)
fields=['occupation','min','max']
writer.writerow(fields)
for occ in sortedkeys:
    row=[occ,occupationminage[occ],occupationmaxage[occ]]
    writer.writerow(row)
f.close()

