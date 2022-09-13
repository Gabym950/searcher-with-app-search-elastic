import unittest

from adapters.publication_adapter import PublicationAdapter
from strategies.elastic_search import ElasticSearch
from searcher import Searcher

class TestAddElastic(unittest.TestCase):

    def setUp(self):
        self.searcher = Searcher(ElasticSearch())

    def test_add(self):
        publication = {
            'title': 'title one',
        }
        result = self.searcher.add(
            article=PublicationAdapter(publication),
            engine='articles',
        )
        self.assertEqual(result,  'Voy a agregar TITLE ONE en articles')
    

    def test_add_multiple(self):
        articles = [
            PublicationAdapter({'title': 'title one'}),
            PublicationAdapter({'title': 'title two'}),
        ]
        result = self.searcher.add_multiple(
            articles=articles,
            engine='articles',
        )
        self.assertEqual(result, "Voy a agregar ['TITLE ONE', 'TITLE TWO'] en articles")


if __name__ == '__main__':
    unittest.main()