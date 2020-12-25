import csv
reader = csv.reader(open('dict.csv', 'r'))
d = {}
for row in reader:
   k, v = row
   d[k] = v
print(d)