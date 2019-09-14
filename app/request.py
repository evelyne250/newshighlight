
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
    # articles_url = app.config['ARTICLES_BASE_URL']
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


# def get_articles(source_id):
#     '''
#     Function that gets articles based on the source id
#     '''
#     get_articles_url = articles_url.format(source_id,api_key)

#     with urllib.request.urlopen(get_articles_url) as url:
#         articles_results = json.loads(url.read())
#         articles_object = None

#         if articles_results['articles']:
#             articles_object = process_articles(articles_results['articles'])
        
#     return articles_object

# def process_articles(articles_list):
#     '''
#     Function that processes the json results for the articles
#     '''
#     article_object = []
    
#     for article_item in articles_list:
#          id = article_item.get('id')
#          author = article_item.get('author')
#          title = article_item.get('title')
#          description = article_item.get('description')
#          url = article_item.get('url')
#          image = article_item.get('urlToImage')
#          date = article_item.get('publishedAt')
#          if image:
#             articles_result = Articles(id,author,title,description,url,image,date)
#             articles_object.append(articles_result)
#     return articles_object



# import urllib.request,json

# from .models import Source,Articles

# api_key=None

# base_url_source=None

# base_url_articles=None

# def configure_request(app):
#     global api_key,base_url_source,base_url_articles
#     api_key = app.config['NEWS_API_KEY']
#     base_url_source=app.config['BASE_URL_SOURCES']
#     base_url_articles=app.config['BASE_URL_ARTICLES']

# def get_source():
#     '''
#     Function that gets the json response to our url request
#     '''

#     get_source_url = base_url_source.format(api_key)
#     with urllib.request.urlopen(get_source_url) as url:
#         get_source_data = url.read()
#         get_source_response = json.loads(get_source_data)

#         news_results = None

#         if get_source_response['sources']:
#             source_results_list = get_source_response['sources']
#             source_results = process_results(source_results_list)


#     return source_results


# def process_results(source_list):

#     source_results = []
#     for source_item in source_list:
#         id = source_item.get('id')
#         name = source_item.get('name')
#         description = source_item.get('description')
#         source_object = Source(id,name,description)
#         source_results.append(source_object)
#     return source_results
# def get_articles(id):
#     '''
#     Function that gets the json response to our url request
#     '''

 
#     get_articles_url = base_url_articles.format(id,api_key)
#     with urllib.request.urlopen(get_articles_url) as url:
#         get_articles_data = url.read()
#         get_articles_response = json.loads(get_articles_data)

#         articles_results = None

#         if get_articles_response['articles']:
#             articles_results_list = get_articles_response['articles']
#             articles_results = process_article_results(articles_results_list)
           
#     return articles_results


# def process_article_results(articles_list):

#     articles_results = []
#     for article_item in articles_list:
#         source=article_item.get('source')
#         author=article_item.get('author')
#         title=article_item.get('title')
#         description=article_item.get('description')
#         url=article_item.get('url')
#         urlToImage=article_item.get('urlToImage')
#         publishedAt=article_item.get('publishedAt')


#         articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
#         articles_results.append(articles_object)
#     return articles_results