import unittest
from models import headlines

Headlines = headlines.Headlines
Sources = headlines.Sources


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
