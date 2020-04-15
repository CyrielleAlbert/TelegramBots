import requests

def get_news_from_keyword(apikey,keyword):
    news_api_url = ('http://newsapi.org/v2/everything?'
                    'qInTitle='+ str(keyword)+'&'
                    'sortBy=relevancy&'
                    'apiKey=' + str(apikey))
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
def get_news_from_country(apikey, country_code):
    news_api_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=' + str(country_code)+'&'
                    'apiKey=' + str(apikey))
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
