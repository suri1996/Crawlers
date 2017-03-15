import scrapy
import pandas as pd
import pkgutil
from io import StringIO

class StocksSpider(scrapy.Spider):

    name="articles"

    raw = pkgutil.get_data("articles", "res/links.csv")
    csvio = StringIO(unicode(raw))
    array = pd.read_csv(csvio, index_col = False)

    start_urls = ['http://www.cnbc.com/2017/01/31/the-associated-press-1-800-flowerscom-misses-street-2q-forecasts.html']

    array_count = 2
    article_count = 1

    def parse(self, response):

        yield {
            'Article': self.article_count,
        }

        for paragraph in response.css("div.group p"):
            yield{
                'paragraph': paragraph.css("p").extract_first(),
            }

        self.array_count+=1
        self.article_count+=1
        while 'http' not in self.array.href[self.array_count]:
            yield {
                'name': self.array.href[self.array_count]
            }
            self.array_count += 1
            self.article_count = 1
        next_page = self.array.href[self.array_count]
        yield scrapy.Request(next_page,callback=self.parse, dont_filter = True)