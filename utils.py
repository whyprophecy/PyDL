import requests
import json


class item:
    def __init__(self, name='Name', itemid='ID', quote='Quote', imageurl='', description='Description'):
        self.name = name
        self.itemid = itemid
        self.quote = quote
        self.imageurl = imageurl  # this url directly points to the image
        self.description = description

    def search(self, searchcontent):
        searchresult = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&list=search&format=json&srsearch=%s&srlimit=1' % searchcontent)
        # use mediawiki api to search
        js = json.loads(searchresult.text)
        self.name = js['query']['search'][0]['title']
        pageid = js['query']['search'][0]['pageid']
        maincontent = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=revisions&format=json&titles=%s&rvprop=content' % self.name)
        # use mediawiki api to acquire the content of the page describing the item
        js = json.loads(maincontent.text)
        contentlist = js['query']['pages']['%d' %
                                           pageid]['revisions'][0]['*'].split('\n')
        # grab the useful imformation and split it for further processing
        for each in contentlist:
            if each.find('id') != -1:
                self.itemid = each.split('= ')[1]
            if each.find('quote') != -1:
                self.quote = each.split('= ')[1]
            if each.find('description') != -1:
                self.description = each.split('= ')[1].replace(
                    '[[', '').replace(']]', '')  # use 'replace' to remove the unnecessary characters in wikitext
                break
        imagelist = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&prop=images&format=json&titles=%s' % self.name)
        # use mediawiki api to acquire the imagelists used on the page
        js = json.loads(imagelist.text)
        for each in js['query']['pages']['%d' % pageid]['images']:
            if each['title'].find('%s' % self.name+' icon') != -1:
                imagename = each['title']
                # get the specific image's name we want
        imageinfo = requests.get(
            'https://bindingofisaacrebirth.fandom.com/api.php?action=query&format=json&titles=%s&prop=imageinfo&iiprop=url' % imagename)
        # use mediawiki api to acquire the url of that specific image using its name
        js = json.loads(imageinfo.text)
        for imageid in js['query']['pages']:  # use this loop to skip through a dict
            pass
        self.imageurl = js['query']['pages']['%s' %
                                             imageid]['imageinfo'][0]['url']


if __name__ == '__main__':
    ex = item()
    ex.search('golden razor')
    print(ex.name, ex.itemid, ex.quote, ex.imageurl, ex.description)
