import json
import csv

f = open('stdv/data.json','r')
x = json.loads(f.read())

f = csv.writer(open("data.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["desc", "price", "link"])

for x in x:
	f.writerow([
		x['desc'],
		x['price'],
		x['link']])
