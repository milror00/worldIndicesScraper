import lxml
import requests
import urllib3
from io import BytesIO
from lxml import etree
from lxml import html

"""
Class description:
Get financial currency data from Yahoo finance and save it to db.

Author:
Rob Milroy

Website:
https://pyscrape.com

Modify:
2020-04-26
"""


class YahooWorldIndices:
    def __init__(self):
        self.url = "https://finance.yahoo.com/world-indices"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 "
            "Safari/537.36",
        }

    def getURL(self):
        try:
            http = urllib3.PoolManager()
            self.response = http.request("GET", self.url)
        except Exception as e:
            print(e)
            exit(1)

    def getAllTableRows(self):
        dom = lxml.html.parse(BytesIO(self.response.data))
        # all table rows
        xpatheval = etree.XPathDocumentEvaluator(dom)
        rows = xpatheval("//table/tbody/tr")
        return rows

    def getRowIndex(self, row):
        index = {}
        columns0 = row.findall("td/a")
        columns1 = row.findall("td")
        columns2 = row.findall("td/span")

        index["symbol"] = columns0[0].text
        index["name"] = columns1[1].text
        index["lastPrice"] = columns1[2].text
        index["change"] = columns2[0].text
        index["%change"] = columns2[1].text
        index["volume"] = columns1[5].text
        return index

    def getAllWorldIndices(self):
        self.getURL()
        rows = self.getAllTableRows()
        results = []
        index = {}
        for row in rows:
            index = self.getRowIndex(row)
            results.append(index)
        return results


if __name__ == "__main__":
    indices = YahooWorldIndices()
    results = indices.getAllWorldIndices()
    # headers
    print(
        "|{0: <10}|{1: <40}|{2: <15}|{3: <15}|{4: <15}|".format(
            "Symbol", "Name", "Last Price", "Change", "%change"
        )
    )
    print(
        "|----------|-------------------|---------------|"
        "---------------|---------------|"
    )
    # data
    for currency in results:
        print(
            "|{0: <10}|{1: <20}|{2: <15}|{3: <15}|{4: <15}|".format(
                currency["symbol"],
                currency["name"],
                currency["lastPrice"],
                currency["change"],
                currency["%change"],
            )
        )
