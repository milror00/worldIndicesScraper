import lxml
import urllib3

from features.pages.Page import Page
from io import BytesIO
import urllib3
from lxml import etree
from lxml import html


class WorldIndicesPage(Page):

    def __getTableRowByIndexSymbol__(self, context, symbol):
        rows = self.__getAllTableRows__(context)
        index = {}
        for row in rows:
            index = self.__getRowIndex(row)
            if (index['symbol'] == symbol):
                return index
        return index

    def getWorldIndexDataBySymbol(self, context, symbol):
        index = self.__getTableRowByIndexSymbol__(context, symbol)
        return context.indices.append(index)

    def getAllWorldIndices(self, context):
        rows = self.__getAllTableRows__(context)
        index = {}
        for row in rows:
            index = self.__getRowIndex(row)
            context.indices.append(index)

    def __getAllTableRows__(self, context):
        dom = lxml.html.parse(BytesIO(context.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        rows = xpatheval('//table/tbody/tr')
        return rows

    def __getRowIndex(self, row):
        index = {}
        columns0 = row.findall("td/a")
        columns1 = row.findall("td")
        columns2 = row.findall("td/span")

        index['symbol'] = columns0[0].text
        index['name'] = columns1[1].text
        index['lastPrice'] = columns1[2].text
        index['change'] = columns2[0].text
        index['%change'] = columns2[1].text
        index['volume'] = columns1[5].text
        return index



