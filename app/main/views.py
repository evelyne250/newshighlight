from flask import render_template
from . import main
from ..request import get_sources
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
    return render_template('index.html',title = title)