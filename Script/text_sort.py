import csv


def getKey(item):
	return item[1]



a = []

with open('./part-00000','r') as f:
	reader = csv.reader(f, dialect='excel',delimiter='\t')
	for row in reader:
		a.append(row)

for i in a:
	i[1] = int(i[1])
f.close()

#print(a)

a1 = sorted(a,key=getKey, reverse = True)
#print(a1)

#for i in range(20):
#		print(a1[i])


with open("output2.csv","wb") as resultFile:
	wr = csv.writer(resultFile, dialect = "excel")
	wr.writerows(a1)
