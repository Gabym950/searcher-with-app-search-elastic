from adapters.adapter import Adapter


class PublicationAdapter(Adapter):
    
    def get_formatted_data(self):
        return self.article['title'].upper()