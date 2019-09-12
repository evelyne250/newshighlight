class Config:
    '''
    General configuration parent class
    '''
    BASE_URL_SOURCES = "https://newsapi.org/v2/sources?apiKey={}"
   # BASE_URL_ARTICLES = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True