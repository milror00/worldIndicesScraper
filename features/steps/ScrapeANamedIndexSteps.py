from behave import given, when, then

from features.configuration.configuration import Configuration
from features.pages.WorldIndicesPage import WorldIndicesPage


@given(u'I am on the yahoo world indices page')
def step_impl(context):
    config = Configuration()
    page = WorldIndicesPage()
    page.getURL(context, config.getBaseURI())

@when(u'I scrape the named index {text}')
def step_impl(context, text):
    page = WorldIndicesPage()
    context.indices = []
    page.getWorldIndexDataBySymbol(context, text)

@when(u'I scrape all the named indices')
def step_impl(context):
    page = WorldIndicesPage()
    context.indices = []
    page.getAllWorldIndices(context)


@then(u'I output the data to the std out')
def step_impl(context):
    for index in context.indices:
        print("Symbol: " + index['symbol'])
        print("Name: " + index['name'])
        print("Last Price: " + index['lastPrice'])
        print("Change: " + index['change'])
        print("% Change: " + index['%change'])
        print("Volume: " +index['volume'])
