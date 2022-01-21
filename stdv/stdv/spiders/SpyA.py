import scrapy
import json


class SpyA(scrapy.Spider):
	name = "spy"
	
	def __init__(self, url = None, *args, **kwargs):
		super(SpyA, self).__init__(*args, **kwargs)
		self.start_urls = [f'{url}']

	def __jHandler(self): 

		f = open('params.json', 'r') 
		data = json.loads(f.read()) 

		return data['params']
	
	
	def parse(self, response):
		data = self.__jHandler()	
	
		r1 = response.css('div.offer-item__content')
		for x in r1:
			links =  x.css(data['link']).get()
				
			yield {
				'title': x.css(data['desc']).get().strip(),
				'price': float(x.css(data['price']).get().strip().replace(',', '.')),
				'link': links
			}
			
		r2 = response.css('li.next')
		
		nPageUrl = r2.css('a::attr("href")').get()
		nPageNr = int(nPageUrl[-1])
		
		if nPageUrl is not None and nPageNr < 3:
			yield response.follow(nPageUrl, self.parse)
