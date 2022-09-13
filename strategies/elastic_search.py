from searcher_strategy import SearcherStrategy


class ElasticSearch(SearcherStrategy):
 
    def __init__(self):
        self.search_obj = {}

    def search(self, engine, key_word):
        return f'Voy a buscar {key_word} en {engine}'

    def add(self, engine, article):
        data = article.get_formatted_data()
        return f'Voy a agregar {data} en {engine}'

    def add_multiple(self, engine, articles):
        data = []
        for article in articles:
            data.append(article.get_formatted_data())
        return f'Voy a agregar {data} en {engine}'
