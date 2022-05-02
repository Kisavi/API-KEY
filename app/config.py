class Config:
    """
    General configuration parent class
    """
    HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'


class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG = True
