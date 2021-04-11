import requests
import json
from PIL import Image


class item:
    def __init__(self, name='Name', itemid='ID', quote='Quote', imageurl='', description='Description'):
        self.name = name
        self.itemid = itemid
        self.quote = quote
        self.imageurl = imageurl
        self.description = description

    def search(self, searchcontent):
        searchresult = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&list=search&format=json&srsearch=%s&srlimit=1' % searchcontent)
        js = json.loads(searchresult.text)
        self.name = js['query']['search'][0]['title']
        pageid = js['query']['search'][0]['pageid']
        maincontent = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=revisions&format=json&titles=%s&rvprop=content' % self.name)
        js = json.loads(maincontent.text)
        contentlist = js['query']['pages']['%d' %
                                           pageid]['revisions'][0]['*'].split('\n')[1:4]
        self.itemid = contentlist[0].split('= ')[1]
        self.quote = contentlist[1].split('= ')[1]
        self.description = contentlist[2].split(
            '= ')[1].replace('[[', '').replace(']]', '')
        imagelist = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=images&format=json&titles=%s' % self.name)
        js = json.loads(imagelist.text)
        for each in js['query']['pages']['%d' % pageid]['images']:
            if each['title'].find('%s' % self.name+' icon') != -1:
                imagename = each['title']
        imageinfo = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&format=json&titles=%s&prop=imageinfo&iiprop=url' % imagename)
        js = json.loads(imageinfo.text)
        for imageid in js['query']['pages']:
            pass
        self.imageurl = js['query']['pages']['%s' %
                                             imageid]['imageinfo'][0]['url']


if __name__ == '__main__':
    ex = item()
    ex.search('blank card')
    print(ex.name, ex.itemid, ex.quote, ex.imageurl, ex.description)
#itemimage = Image.open(requests.get(self.imageurl, stream=True).raw)
