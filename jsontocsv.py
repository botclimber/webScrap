import json
import csv

class jsontocsv:
	read_from = '../data/data.json'	
	write_in = '../data/data.csv' 	

	def __init__(self):
			
		f = open(read_from, 'r')
		self.x = json.loads(f.read())

	def convert(self):
		
		f = csv.writer(open(write_in ,"w", newline=''))

		# Write CSV Header, If you dont need that, remove this line
		f.writerow(["title", "price", "link"])

		for x in x:
			f.writerow([
				x['title'],
				x['price'],
				x['link']])

