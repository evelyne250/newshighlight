
import urllib.request,json
from .models import Sources,Articles

# News = news.News

# Getting api key
api_key = None
# Getting the movie base url
articles_url = None

def configure_request(app):
    global api_key, sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    
    return sources_results

def process_results(sources_list):
    '''
    Function that processes the sources results
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Sources(id,name,description,url,category,language,country)
            sources_results.append(source_object)
            
    return sources_results


def get_articles(source_id,limit):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id,limit,api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])
        
    return articles_location_results

def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []
    
    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]),month=int(date_published[5:7]),day=int(date_published[8:10]),hour=int(date_published[11:13]),minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(author,title,description,url,urlToImage,publishedAt)
            article_location_list.append(article_source_object)
        
    return article_location_list
# def process_articles(articles_list):
#     '''
#     Function that processes the json results for the articles
#     '''
#     article_object = []
    
#     for article_item in articles_list:
#          name = article_item.get('name')
#          author = article_item.get('author')
#          title = article_item.get('title')
#          description = article_item.get('description')
#          url = article_item.get('url')
#          urlToImage = article_item.get('urlToImage')
#          date = article_item.get('publishedAt')
#          content = article_item.get('content')
#          if image:
#             articles_result = Articles(name,author,title,description,url,urlToImage,date, content)
#             articles_object.append(articles_result)
#     return articles_object



