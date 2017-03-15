import scrapy

class StocksSpider(scrapy.Spider):
	name="Companies"

	token = 65
	start_urls = ['http://www.nasdaq.com/screening/companies-by-name.aspx?letter=A&pagesize=200']

	def parse(self,response):
		c=0
		for row in response.css('div.genTable table tr'):
			c=c+1
			if(c%2==0):
				yield {
					'Name': row.css('td a::text').extract_first(),
					'Symbol': row.css('td h3 a::text').extract_first(),
					'Market Cap': row.css('td::text')[2].extract(),
				}
		if int(response.xpath('//*[@id="resultsDisplay"]/small/b[2]/text()').extract_first())>200 and not 'pagerlinkd' in response.xpath('//*[@id="two_column_main_content_lb_NextPage"]').extract_first():
			next_page = response.xpath('//*[@id="two_column_main_content_lb_NextPage"]//@href').extract_first()
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)
		elif self.token<90:
			self.token += 1
			next_page = 'http://www.nasdaq.com/screening/companies-by-name.aspx?letter='+chr(self.token)+'&pagesize=200'
			yield scrapy.Request(next_page, callback=self.parse)
