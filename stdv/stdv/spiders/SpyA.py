import scrapy
import json
import re

class SpyA(scrapy.Spider):
	name = "spy"
	
	def __init__(self, *args, **kwargs):
		super(SpyA, self).__init__(*args, **kwargs)
		
		#self.start_urls = self.__urls()
		self.start_urls = ["https://ruisilauto.standvirtual.com/"]
		self.brands = self.__extractBrands()		

	
	def __urls(self):

		urls_file = open('sites_test.txt', 'r')
		urls = [x for x in urls_file.readlines()]
		urls_file.close()	
	
		return urls

	def __extractBrands(self):
		text_file = open('marcas.txt', 'r')
		
		brands = []
		for x in text_file.readlines():
			brands.append(x.lower().replace('\n',''))
		
		text_file.close()

		return brands


	def __jHandler(self): 

		f = open('params.json', 'r') 
		data = json.loads(f.read()) 

		return data['params']

	def __extract(self, data):
		
		dataBrand = data.lower() # with this we only parse the string to lower once
		brand = 'Not found'	
		for x in self.brands:
			if x in dataBrand:
				brand = x
				break
		
		yearM1 = re.search("\[[0-9]+_[0-9]+", data)
		yearM2 = re.search("[0-9]{4} a [0-9]{1,4}", data)

		if yearM1:
			year = yearM1.group().replace('[','')
			year = year.split('_')
		
		elif yearM2:
			year = yearM2.group().replace('a','')
			year = year.split()	
		
		else:
			year = [None, None]		

		return data, brand, year
			
	
	def parse(self, response):
		data = self.__jHandler()	

		links = response.css('div.ooa-t4nnij a::attr(href)').getall()	
		titles = response.css('div.ooa-1856yh h3::text').getall()
		price = response.css('div.ooa-uw5svp p::text').getall()
		price = [x for x in price[::2]]

		for x in range(len(title)):
			
			title, brand, year = self.__extract(titles[x])		
			
			yield {
				'title': title,
				'brand': brand,
				'price': float(price[x].replace(',', '.').replace(' ','.')),
				'start_year': year[0],
				'end_year': year[1],
				'link': links[x]
			}
			
		r2 = response.css('li.next')
		nPageUrl = r2.css('a::attr("href")').get()
		
		if nPageUrl is not None:
			yield response.follow(nPageUrl, self.parse)



