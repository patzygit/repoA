from compare import *
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
    generateFileJson("data/", "dataRootIdItems", context.response.json())

#/items/10048278/DoneRootItem.json
@given(u'I have a service with item id "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod
#failed
@when(u'I send {method} item request to get root parent for done item')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    print ("////", context.response)
    generateFileJson("data/", "dataDRootIdItems", context.response.json())
