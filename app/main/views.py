from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_headlines, get_sources


@main.route('/')
def index():
    news_headlines = get_headlines()
    return render_template('index.html', headlines=news_headlines)


@main.route('/sources')
def source():
    news_sources = get_sources()
    return render_template('sources.html', sources=news_sources)
