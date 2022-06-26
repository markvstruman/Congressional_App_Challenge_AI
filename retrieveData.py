import os
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import html2text

api = NewsApiClient(api_key='c8b7f53e7eca48adae6cdcc7e7361ea7')
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent':user_agent}
API_request = api.get_everything(q='politics',
                                     # sources='bbc-news,the-verge',
                                     # domains='bbc.co.uk,techcrunch.com',
                                      from_param='2022-05-26',
                                      to='2022-06-26',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

numberOfArticles = len(API_request['articles'])
articleCount = 0
urlList = []
for i in API_request['articles']:
    urlList.append(API_request['articles'][articleCount]['url'])
    articleCount = articleCount+1

articleCount = 0
print(urlList[articleCount])
for i in urlList:
    req = Request(urlList[articleCount], None, headers)
    try:
        html_page = urlopen(req)
    except:
        print("It's probably a dead-link")
        continue

    soup = BeautifulSoup(html_page, "html.parser")
    
    text = html2text.HTML2Text()
    text.ignore_links = True
    f = open("articles/article%d.txt" % articleCount, 'w', encoding="utf-8")

    for line in text.handle(str(soup)):
        try:
            f.write(line)
        except:
            print("Wow, an error")
        finally:
            continue
    f.close()
    articleCount = articleCount+1
