import requests
import json


class item:
    def __init__(self, name='', quote='', imageurl='', description=''):
        self.name = name
        self.quote = quote
        self.imageurl = imageurl
        self.description = description

    def __str__(self):
        return '%s\n%s\n%s\n%s\n%s\n' % (self.name, self.quote, self.imageurl, self.description)


obj = item
researchcontent = 'a pony'
researchresult = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&list=search&format=json&srsearch=%s&srlimit=1' % researchcontent)

