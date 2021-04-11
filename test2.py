import requests
import json
from PIL import Image


class item:
    def __init__(self, name='', itemid='', quote='', imageurl='', description=''):
        self.name = name
        self.itemid = itemid
        self.quote = quote
        self.imageurl = imageurl
        self.description = description

    def __str__(self):
        return '%s\n%s\n%s\n%s\n%s\n' % (self.name, self.itemid, self.quote, self.imageurl, self.description)


obj = item
researchcontent = 'crack the sky'
researchresult = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&list=search&format=json&srsearch=%s&srlimit=1' % researchcontent)
js = json.loads(researchresult.text)
obj.name = js['query']['search'][0]['title']
pageid = js['query']['search'][0]['pageid']
maincontent = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=revisions&format=json&titles=%s&rvprop=content' % obj.name)
js = json.loads(maincontent.text)
contentlist = js['query']['pages']['%d' %
                                   pageid]['revisions'][0]['*'].split('\n')[1:4]
obj.itemid = contentlist[0].split('= ')[1]
obj.quote = contentlist[1].split('= ')[1]
obj.description = contentlist[2].split(
    '= ')[1].replace('[[', '').replace(']]', '')
imagelist = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=images&format=json&titles=%s' % obj.name)
js = json.loads(imagelist.text)
for each in js['query']['pages']['%d' % pageid]['images']:
    if each['title'].find('%s' % obj.name+' icon') != -1:
        imagename = each['title']
imageinfo = requests.get(
    'https://bindingofisaacrebirth.fandom.com/api.php?action=query&format=json&titles=%s&prop=imageinfo&iiprop=url' % imagename)
js = json.loads(imageinfo.text)
for imageid in js['query']['pages']:
    pass
obj.imageurl = js['query']['pages']['%s' % imageid]['imageinfo'][0]['url']
itemimage = Image.open(requests.get(obj.imageurl, stream=True).raw)

