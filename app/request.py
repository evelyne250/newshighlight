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
            sources_results = process_results(get_sources_response['sources'])
    
    return sources_results
