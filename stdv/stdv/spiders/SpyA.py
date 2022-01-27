import scrapy
import json
import re

class SpyA(scrapy.Spider):
	name = "spy"
	
	def __init__(self, url = None, *args, **kwargs):
		super(SpyA, self).__init__(*args, **kwargs)
		self.start_urls = [f'{url}']
					
		self.brands = self.__extractBrands()		


	def __extractBrands(self):
		text_file = open('marcas.txt', 'r')
		
		brands = []
		for x in text_file.readlines():
			brands.append(x.replace('\n',''))
		
		text_file.close()

		return brands


	def __jHandler(self): 

		f = open('params.json', 'r') 
		data = json.loads(f.read()) 

		return data['params']

	def __extract(self, data):
		
		brand = 'Not found'	
		for x in self.brands:
			if x in data:
				brand = x
				break

		year = re.search("\[[0-9]+_[0-9]+", data)

		if year:
			year = year.group().replace('[','')
			year = year.split('_')
		else:
			year = [None, None]		

		return data, brand, year
			
	
	def parse(self, response):
		data = self.__jHandler()	
	
		r1 = response.css('div.offer-item__content')
		for x in r1:
			
			links =  x.css(data['link']).get()
			title, brand, year = self.__extract(x.css(data['title']).get().strip())		
			
			yield {
				'title': title,
				'brand': brand,
				'price': float(x.css(data['price']).get().strip().replace(',', '.').replace(' ','.')),
				'start_year': year[0],
				'end_year': year[1],
				'link': links
			}
			
		r2 = response.css('li.next')
		
		nPageUrl = r2.css('a::attr("href")').get()
		nPageNr = int(nPageUrl[-1])
		
		if nPageUrl is not None and nPageNr < 5:
			yield response.follow(nPageUrl, self.parse)



