

class Searcher:

    def __init__(self, service):
        self.__service = service

    def search(self, *args, **kwargs):
        return self.__service.search(*args, **kwargs)

    def add(self, *args, **kwargs):
        return self.__service.add(*args, **kwargs)

    def add_multiple(self, *args, **kwargs):
        return self.__service.add_multiple(*args, **kwargs)