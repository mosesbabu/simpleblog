import urllib.request,json
from config import Config
from .models import Quotes

quotes_url = Config['QUOTES_URL']
def get_quotes(id):
    
    with urllib.request.urlopen(quotes_url) as url:
        quotes_data = url.read()
        quotes_response = json.loads(quotes_data)
        
        quote_object=None
        if quotes_response:
            id = quotes_response.get('id')
            author = quotes_response.get('author')
            quote = quotes_response.get('quote')
            permalink = quotes_response.get('permalink')
    
           quote_object = Quotes(author,quote,permalink)
           return quote_object
    
