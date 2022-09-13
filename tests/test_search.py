import unittest

from strategies.elastic_search import ElasticSearch
from searcher import Searcher

class TestSearchElastic(unittest.TestCase):

    def setUp(self):
        self.searcher = Searcher(ElasticSearch())

    def test_search(self):
        result = self.searcher.search(
            key_word='bipolar',
            engine='articles'
        )
        self.assertEqual(result, 'Voy a buscar bipolar en articles')


if __name__ == '__main__':
    unittest.main()