import scrapy
import json
import re

class SpyA(scrapy.Spider):
	name = "spy_test"

	def __init__(self, *args, **kwargs):
		super(SpyA, self).__init__(*args, **kwargs)

		self.start_urls = ['https://ruisilauto.standvirtual.com/']


	def parse(self, response):

		links = response.css('div.ooa-t4nnij a::attr(href)').getall()
		data = response.css('div.ooa-1856yh h3::text').getall()
		price = response.css('div.ooa-uw5svp p::text').getall()
		price = [x for x in price[::2]]
		print(price)
		'''
		for x in r1:

			links =  x.css().get()

			yield {
				'link': links
			}
		'''
