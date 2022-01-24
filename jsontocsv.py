import json
import csv
import sys

class jsontocsv:
	
	def __init__(self, file):
			
		f = open(file, 'r')
		
		self.data = json.loads(f.read())
		self.params = [x for x in self.data[0]]
		
		f.close
		
	def convert(self):
		
		f = csv.writer(open('data.csv',"w", encoding="utf-8", newline=''))

		f.writerow(self.params)
		
		for x in self.data:
			content = [x[y] for y in self.params]			
			f.writerow(content)


if __name__ == "__main__":
	x = jsontocsv(sys.argv[1])
	x.convert()
