from nntplib import ArticleInfo
import os
import newsapi
from newsapi.newsapi_client import NewsApiClient 
#import newsapi
#from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import newspaper


# These traits are used when you go to a website, it basically confirms your a real user
api = NewsApiClient(api_key='c8b7f53e7eca48adae6cdcc7e7361ea7')
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent}
# Making a call to the newsapi to ask for articles, in this case the query is 'politics'
API_request = api.get_everything(q='election',
                                     # sources='bbc-news,the-verge', # You can specify sources
                                      domains='foxnews.com, cnn.com, thefederalist.com, washingtonpost.com, huffpost.com, infowars.com, occupydemocrats.com, americanlibertyreportnews.com', # Or domains
                                      from_param='2022-11-28', # The dates your pulling between
                                      to='2022-12-02',
                                      language='en',
                                      sort_by='relevancy'
                                      #country='us'
                                      #page=2
                                      )

# Making a list of the articles' urls to parse for their HTML
numberOfArticles = len(API_request['articles']) 
articleCount = 380
urlList = []
articleOn = 0

for i in API_request['articles']:
    urlList.append(API_request['articles'][articleOn]['url'])
    if(API_request['articles'][articleOn]['url'].__contains__('foxnews')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('thefederalist')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('infowars')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('americanlibertyreportnews')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('cnn')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('washingtonpost')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('huffpost')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('occupydemocrats')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    articleCount = articleCount+1
    articleOn=articleOn+1

articleCount = articleCount-numberOfArticles

# For every url, do these things
for i in urlList:
    #req = Request(urlList[articleCount], None, headers)
    # try to open the web page with an HTTP request
    f = open("Congressional_App_Challenge_AI/articles/article%d.txt" % articleCount, 'w+', encoding="utf-8")
    
    try:
        article_name = newspaper.Article(url=urlList[articleCount], language="en")
        article_name.download()
        article_name.parse()
        f.write(article_name.text)
        
    except:
        print("Error opening link, probably dead")
        continue
    f.close()
    articleCount = articleCount+1
# new request

API_request = api.get_everything(q='election',
                                     # sources='bbc-news,the-verge', # You can specify sources
                                      domains='foxnews.com, cnn.com, thefederalist.com, washingtonpost.com, huffpost.com, infowars.com, occupydemocrats.com, americanlibertyreportnews.com', # Or domains
                                      from_param='2022-12-03', # The dates your pulling between
                                      to='2022-12-06',
                                      language='en',
                                      sort_by='relevancy'
                                      #country='us'
                                      #page=2
                                      )

# Making a list of the articles' urls to parse for their HTML
numberOfArticles = len(API_request['articles']) 
articleOn = 0
for i in API_request['articles']:
    urlList.append(API_request['articles'][articleOn]['url'])
    if(API_request['articles'][articleOn]['url'].__contains__('foxnews')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('thefederalist')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('infowars')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('americanlibertyreportnews')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('cnn')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('washingtonpost')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('huffpost')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    if(API_request['articles'][articleOn]['url'].__contains__('occupydemocrats')):
        g = open("Congressional_App_Challenge_AI/articleBiases/article%dBias.txt" % articleCount, 'w+', encoding="utf-8")
        g.write("-1")
        g.close()
    articleCount = articleCount+1
    articleOn=articleOn+1

articleCount = articleCount-numberOfArticles

# For every url, do these things
for i in urlList:
    #req = Request(urlList[articleCount], None, headers)
    # try to open the web page with an HTTP request
    f = open("Congressional_App_Challenge_AI/articles/article%d.txt" % articleCount, 'w+', encoding="utf-8")
    
    try:
        article_name = newspaper.Article(url=urlList[articleCount], language="en")
        article_name.download()
        article_name.parse()
        f.write(article_name.text)
        
    except:
        print("Error opening link, probably dead")
        continue
    f.close()
    articleCount = articleCount+1

# new request

