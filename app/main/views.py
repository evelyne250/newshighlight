from flask import render_template
from . import main
from ..request import get_sources, get_articles
from ..models import Sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    new_general = get_sources('general')
    new_business = get_sources('business')
    new_entertainment = get_sources('entertainment')
    new_sports = get_sources('sports')
    new_tech = get_sources('technology')
    new_science = get_sources('science')
    new_health = get_sources('health')

    title = 'Home | Best News Highlight'
    return render_template('index.html',title = title,new_general = new_general, new_business = new_business, new_entertainment = new_entertainment, new_sports = new_sports, new_tech = new_tech, new_science = new_science, new_health = new_health)


@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles based on their sources
    '''
    print(source_id)
    # per_page = 40
    news_source = get_articles('source_id')
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id,news_source = news_source)

