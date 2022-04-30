from app import app
import urllib.request, json
from .models import news

api_key = app.config['NEWS_API_KEY']

base_url = app.config['HEADLINES_API_BASE_URL']
