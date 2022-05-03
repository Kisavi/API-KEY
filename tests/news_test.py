import unittest
from app.models import Headlines, Sources


# test for headlines class
class HeadlinesTest(unittest.TestCase):
    """
    Test case to test the behaviour of the Headlines class
    """

    def setUp(self):
        """
        This method runs before every case
        """

        self.new_headlines = Headlines('bbc-news', 'John', 'War in Ukraine', 'The war that Putin is not ready to lose',
                                       'https://www.washingtonpost.com/politics/2022/05/02/biden-javelins-first-lady-refugees/',
                                       '"https://images.wsj.net/im-535503/social', '2022-05-02T13:16:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headlines, Headlines))


if __name__ == '__main__':
    unittest.main()


# test for the sources class
class SourcesTest(unittest.TestCase):
    """
    Test case to test the behaviour of the Sorces class
    """

    def setUp(self):
        """
        This method runs before every case
        """

        self.new_sources = Sources("ABC News",
                                   "Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur.",
                                   "https://www.aftenposten.no")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))
