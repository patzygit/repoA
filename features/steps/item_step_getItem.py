from compare import *
from jsondiff import diff
from utils.json_order import *

from utils.module_rest import *
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
    generateFileJson("data/", "dataAllItems", context.response.json())

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
    generateFileJson("data/", "dataIdItems", context.response.json())

@then(u'response body should contain item information of specified item as')
def step_impl(context):
    context.response_get = json.loads(context.text)
    #print ("***//data", context.response_get)
    #print ("repons -re " , context.response.json())
    boolean = ordered(context.response_get) != ordered(context.response.json())
    #print ("bool",boolean)
    assert boolean == True
 #   expect(int(context.response_get)).to_equal(context.response.json())

@then(u'response body should empty of specified item as')
def step_impl(context):
 a=diff(context.text,context.response)
 print ("text", a)
 expect(a).to_equal({})

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
    print ("rootId",context.response)
    generateFileJson("data/", "dataRootIdItems", context.response.json())

@then(u'response body should contain item information of unchecked item as')
def step_impl(context):
    context.response_get = json.loads(context.text)
    #print ("***//data", context.response_get)
    #print ("repons -re " , context.response.json())
    boolean = ordered(context.response_get) != ordered(context.response.json())
    #print ("bool",boolean)
    assert boolean == True

#/items/10048278/DoneRootItem.json
@given(u'I have a service with item id "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod
#failed
@when(u'I send {method} item request to get an error for done item that does not exist')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    #print ("////", context.response_dr)
    print("////status", context.response.status_code)
   # generateFileJson("data/", "dataDoneRootIdItems", context.response_dr.json())
