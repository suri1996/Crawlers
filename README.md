# Crawlers
The NASDAQ folder has the crawler which crawled the names, symbols and market caps of all companies in NASDAQ.

The 'sa' folder has the crawler which uses the symbols crawled from NASDAQ in the file 'array.csv', and crawls for news articles links on CNBC for those companies. The output is in s.json. There is a python file called 'data_cleaning_links.py' which generates a csv file with the links.

The 'CNBC_articles' folder has the crawler to crawl through the links in links.csv created in 'sa' and stores the paragraphs in each articles as an item.

