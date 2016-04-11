import parser
from html.parser import HTMLParser
from urllib import parse
class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
        
    def handle_starttage(self,tag,attrs):
        if tag == 'a':
            for(attributes,value) in attrs:
                if attributes=='href':
                    url=parse.urljoin(self.base_url,value)
                    self.links.add(url)
                
                
        
        
    def error(self,message):
        pass
    
