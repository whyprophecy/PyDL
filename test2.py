import requests
import json


class item:
    def __init__(self, name='', id='', quote='', imageurl='', description=''):
        self.name = name
        self.id = id
        self.quote = quote
        self.imageurl = imageurl
        self.description = description

    def __str__(self):
        return '%s\n%s\n%s\n%s\n%s\n' % (self.name, self.id, self.quote, self.imageurl, self.description)


obj = item
researchcontent = 'blank card'
researchresult = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&list=search&format=json&srsearch=%s&srlimit=1' % researchcontent)
js = json.loads(researchresult.text)
obj.name = js['query']['search'][0]['title']
obj.id = js['query']['search'][0]['pageid']
maincontent = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=revisions&format=json&titles=%s&rvprop=content' % obj.name)
js = json.loads(maincontent.text)
#print(js['query']['pages']['%d' % obj.id]['revisions'][0]['*'])
imagelist = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=images&format=json&titles=%s' % obj.name)
js = json.loads(imagelist.text)
for each in js['query']['pages']['%d' % obj.id]['images']:
    if each['title'].find('%s' % obj.name+' icon') != -1:
        imagename = each['title']
imageinfo = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&format=json&titles=%s&prop=imageinfo&iiprop=url' % imagename)
js = json.loads(imageinfo.text)
for imageid in js['query']['pages']:
    pass
obj.imageurl = js['query']['pages']['%s' % imageid]['imageinfo'][0]['url']
print(obj.imageurl)
