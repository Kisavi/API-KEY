from flask import render_template
from app import app
from .request import get_headlines


@app.route('/')
def index():
    news_headlines = get_headlines()
    return render_template('index.html', headlines=news_headlines)


