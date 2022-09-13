class Adapter():

    def __init__(self, article):
        self.__article = article

    @property
    def article(self):
        return self.__article

    def get_formatted_data(self):
        raise NotImplementedError()
