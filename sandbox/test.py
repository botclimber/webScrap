import json





class Helper:

	def jHandler(self):
		
		f = open('params.json', 'r')
		data = json.loads(f.read())
		
		return data


x = Helper()
print(x.jHandler())
