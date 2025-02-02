import os

class Config:
    '''
    General configuration for the parent class
    '''
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = '77ea22a21b0f47acb4283a1e4d5813f3'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


