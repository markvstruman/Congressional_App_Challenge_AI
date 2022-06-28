from nntplib import ArticleInfo
import os
from newsapi.newsapi_client import NewsApiClient 
#import newsapi
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import newspaper


# These traits are used when you go to a website, it basically confirms your a real user
api = NewsApiClient(api_key='c8b7f53e7eca48adae6cdcc7e7361ea7')
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent}
# Making a call to the newsapi to ask for articles, in this case the query is 'politics'
API_request = api.get_everything(q='politics',
                                     # sources='bbc-news,the-verge', # You can specify sources
                                     # domains='bbc.co.uk,techcrunch.com', # Or domains
                                      from_param='2022-05-27', # The dates your pulling between
                                      to='2022-06-27',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# Making a list of the articles' urls to parse for their HTML
numberOfArticles = len(API_request['articles']) 
articleCount = 0
urlList = []
for i in API_request['articles']:
    urlList.append(API_request['articles'][articleCount]['url'])
    articleCount = articleCount+1



articleCount = 0
# For every url, do these things
for i in urlList:
    #req = Request(urlList[articleCount], None, headers)
    # try to open the web page with an HTTP request
    f = open("articles/article%d.txt" % articleCount, 'w', encoding="utf-8")
    
    try:
        article_name = newspaper.Article(url=urlList[articleCount], language="en")
        article_name.download()
        article_name.parse()
        f.write(article_name.text + "\n\nURL: " + urlList[articleCount] + "\n\nTITLE: " + article_name.title)
        
    except:
        print("Error opening link, probably dead")
        continue
    f.close()
    articleCount = articleCount+1
