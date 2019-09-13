from app import app
from app import app
import urllib.request,json
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
sources_url = app.config["BASE_URL_SOURCES"]
#articles_url = app.config["BASE_URL_ARTICLES"]

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

        # if url:
        #     source_object = Sources(id,name,description,url,category,language,country)
        #     sources_results.append(source_object)
            
    return sources_results
