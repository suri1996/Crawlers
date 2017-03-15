import scrapy
import pandas as pd

class StocksSpider(scrapy.Spider):
	name="sa"

	array = pd.read_csv("array.csv", index_col = False)

	print array.Symbol[0]
	print array

	start_urls = ['http://data.cnbc.com/quotes/MSGN/tab/1?viewtype=more']

	j=4065
	def parse(self,response):
		y = response.css('div.promo div.subsection::text')
		if "There is no recent news" not in y:
			yield {'name': self.array.Symbol[self.j]}
			for news in response.css("div.promo div.subsection ul li div.asset div.headline"):
				x = news.css('span::text').extract_first()
				if '2016' not in x:
					y = news.css('a').extract_first()
					if 'span' not in y:
						yield {
							'href': news.css('a::attr(href)').extract_first(),
						}
				else:
					break
		self.j += 1
		next_page = 'http://data.cnbc.com/quotes/'+self.array.Symbol[self.j]+'/tab/1?viewtype=more'
		yield scrapy.Request(next_page, callback=self.parse)
