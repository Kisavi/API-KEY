class Headlines:

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Sources:

    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

      