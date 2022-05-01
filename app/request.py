from app import app
import urllib.request, json
from .models import news

News = news.News  # variable name News of file news of class News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['HEADLINES_API_BASE_URL']


def get_headlines():
    get_headlines_url = base_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.load(get_headlines_data)

        headlines_results = None

        if get_headlines_response['totalResults']:
            headlines_results_list = get_headlines_response['results']
            headlines_results = process_results(headlines_results_list)

    return headlines_results
