import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html
from features.configuration.configuration import Configuration


class Page:

    def getURL(self, context,  url):
        http = urllib3.PoolManager()
        config = Configuration()
        context.response = http.request('GET',config.getBaseURI())

    def __getTableRowByIndexSymbol__(self, context, symbol):
        rows = self.__getAllTableRows__(context)
        index = {}
        for row in rows:
            index = self.__getRowIndex__(row)
            if (index['symbol'] == symbol):
                return index
        return index

    def __getAllTableRows__(self, context):
        dom = lxml.html.parse(BytesIO(context.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        rows = xpatheval('//table/tbody/tr')
        return rows
