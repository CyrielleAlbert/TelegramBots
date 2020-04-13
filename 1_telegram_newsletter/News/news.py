import requests

def get_news_from_france(apikey):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
           'country=fr&'
           'apiKey='+ str(apikey))
    response = requests.get(news_api_url)
    dict_resp = response.json()
    i = 0
    new_10_articles = []
    while i <= 10:
        for article in dict_resp["articles"]:
            i += 1
            if i > 10 :
                break
            else :
                new_10_articles.append({"title":article["title"],"url":article["url"]})
    return new_10_articles
def get_news_from_uk(apikey):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=gb&'
                    'apiKey='+ str(apikey))
    response = requests.get(news_api_url)
    dict_resp = response.json()
    i = 0
    new_10_articles = []
    while i <= 10:
        for article in dict_resp["articles"]:
            i += 1
            if i > 10:
                break
            else:
                new_10_articles.append({"title": article["title"], "url": article["url"]})
    return new_10_articles
def get_news_from_norway(apikey):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=fr&'
                    'apiKey=' +str(apikey))
    response = requests.get(news_api_url)
    dict_resp = response.json()
    i = 0
    new_10_articles = []
    while i <= 10:
        for article in dict_resp["articles"]:
            i += 1
            new_10_articles.append({"title": article["title"], "url": article["url"]})
    return new_10_articles
def get_news_from_spain(apikey):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=fr&'
                    'apiKey='+str(apikey))
    response = requests.get(news_api_url)
    dict_resp = response.json()
    i = 0
    new_10_articles = []
    while i <= 10:
        for article in dict_resp["articles"]:
            i += 1
            new_10_articles.append({"title": article["title"], "url": article["url"]})
    return new_10_articles
def get_news_from_usa(apikey):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=us&'
                    'apiKey='+str(apikey))
    response = requests.get(news_api_url)
    dict_resp = response.json()
    i = 0
    new_10_articles = []
    while i <= 10:
        for article in dict_resp["articles"]:
            i += 1
            if i > 10:
                break
            else:
                new_10_articles.append({"title": article["title"], "url": article["url"]})
    return new_10_articles