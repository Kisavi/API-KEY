from app import app
import urllib.request, json
from .models import headlines
from .models.headlines import Sources

Headlines = headlines.Headlines  # variable name News of file news of class News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['HEADLINES_API_BASE_URL']

sources_url = app.config['SOURCES_API_BASE_URL']


def get_headlines():
    """
    method to get headlines
    """
    get_headlines_url = base_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        # print(get_headlines_response)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)

    return headlines_results


def process_headlines(get_headlines_response):
    """
    method that processes response from the api call
    """
    headlines_results = []
    for headline_item in get_headlines_response:
        source = headline_item.get('source')
        author = headline_item.get('author')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        title = headline_item.get('title')
        description = headline_item.get('description')
        publishedAt = headline_item.get('publishedAt')

        if urlToImage and author and title:
            headline_object = Headlines(source, author, title, description, url, urlToImage, publishedAt)
            headlines_results.append(headline_object)

    return headlines_results


def get_sources():
    """
    method that gets various news sources
    """

    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # print(get_sources_response)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(get_sources_response):
    """
      method that processes response from the api call
    """
    sources_results = []

    for source_item in get_sources_response:
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item.get('description')

        if name and description and url:
            source_object = Sources(name, description, url)
            sources_results.append(source_object)

    return sources_results

