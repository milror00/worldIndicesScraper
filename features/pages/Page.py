import requests
import urllib3

from features.configuration.configuration import Configuration


class Page:

    def getURL(self, context,  url):
        http = urllib3.PoolManager()
        context.response = http.request('GET',"https://finance.yahoo.com/world-indices")




