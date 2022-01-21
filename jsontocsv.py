import json
import csv
import sys

class jsontocsv:
	
	def __init__(self, file):
			
		f = open(file, 'r')
		self.x = json.loads(f.read())

	def convert(self):
		
		f = csv.writer(open('data.csv',"w", newline=''))

		# Write CSV Header, If you dont need that, remove this line
		f.writerow(["title", "price", "link"])

		for x in self.x:
			f.writerow([
				x['title'],
				x['price'],
				x['link']])

if __name__ == "__main__":
	x = jsontocsv(sys.argv[1])
	x.convert()
