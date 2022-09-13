

class SearcherStrategy:

    def search(self, engine, key_word):
        raise NotImplementedError()
    
    def add(self, engine, article):
        raise NotImplementedError()

    def add_multiple(self, engine, articles):
        raise NotImplementedError()