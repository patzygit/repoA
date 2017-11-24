from compare import *
from utils.json_order import *
from utils.module_rest import *
from utils.file_system import *
from behave import given, when, then

@given(u'I have a service for "{servicemethod}"')
def step_impl(context,servicemethod):
    context.servicemethod = servicemethod


@when(u'I send {method} items request to get all items information')
def step_impl(context,method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Item_GETAllItems", context.response.json())

#/items/10048278.json
@given(u'I have a service with id "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod

@when(u'I send {method} item request to get specified item information')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "Item_GETIdItems", context.response.json())

@then(u'response body should be the same of "{rootFileRIdItem}" with "{rootGetRequest}" for specific item')
def step_impl(context,rootFileRIdItem,rootGetRequest):
    context.rootpathDataFile = FileSystem(rootFileRIdItem)
    context.dataFile = FileSystem(rootGetRequest)
    context.dataFile._print_structure_json
    boolean = context.dataFile._compare_to(context.dataFile._get_DataJson(),context.rootpathDataFile._get_DataJson())
    assert boolean != True
 #   expect(int(context.response_get)).to_equal(context.response.json())

#/items/10028551/RootItem.json
@given(u'I have a service with root id "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod

@when(u'I send {method} item request to get root parent for unchecked item')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    #print ("rootId",context.response)
    generateFileJson("data/", "Item_GETRootIdItems", context.response.json())

@then(u'response body should be the same of "{rootFileRIdItem}" with "{rootGetRequest}" for unchecked item')
def step_impl(context,rootFileRIdItem,rootGetRequest):
    context.rootpathDataFile = FileSystem(rootFileRIdItem)
    context.dataFile = FileSystem(rootGetRequest)
    context.dataFile._print_structure_json
    bool = context.dataFile._compare_to(context.dataFile._get_DataJson(),context.rootpathDataFile._get_DataJson())
    assert bool != True

#/items/10048278/DoneRootItem.json
@given(u'I have a service with item id "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod

@when(u'I send {method} item request to get an error for done item that does not exist')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    #print ("////", context.response_dr)
    print("////status", context.response.status_code)
   # generateFileJson("data/", "dataDoneRootIdItems", context.response_dr.json())

