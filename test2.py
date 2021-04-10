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
obj.name = json.loads(researchresult.text)['query']['search'][0]['title']
maincontent = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=revisions&format=json&titles=%s&rvprop=content' % obj.name)
js = json.loads(maincontent.text)
print(js['query']['pages']['2856']['revisions'][0]['*'])
