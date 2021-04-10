import requests
import json

class item:
    def __init__(self, name='', itemid='', quote='', imageurl='', description=''):
        self.name = name
        self.itemid = itemid
        self.quote = quote
        self.imageurl = imageurl
        self.description = description

    def __str__(self):
        return '%s\n%s\n%s\n%s\n%s\n' % (self.name, self.itemid, self.quote, self.imageurl, self.description)


i = item(1, 2, 3, 4, 5)
print(i)
