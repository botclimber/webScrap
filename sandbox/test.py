import json
import re

class test_extract:
	
	def exp(self):
		text = 'Porta Direita Bmw Z3 Roadster (e36) 1.8 I  '
		
		year = re.search("[*[0-9]+_[0-9]+]*", text)		
		
		# working
		# next steps:
		#	- remove retangle bar
		#	- split by _ charater
		# after these steps u have left start date and right final date
		# see possible fails and prevent them

		if year:
			year  = year.group().replace('[','')
			year  = year.replace(']','')
			year = year.split('_')
			print(year[0])
			print(year[1]) 
		else: print(year)		

	def extract(self):
		text_file = open("m.txt", "r")
	
		lines = []	
		for x in text_file.readlines():
			lines.append(x.replace('\n', ''))
		print(lines)
class Helper:

	def jHandler(self):
		
		f = open('params.json', 'r')
		data = json.loads(f.read())
		
		return data


x = test_extract()
#x.extract()
x.exp()

#x = Helper()
#print(x.jHandler())
