from compare import *
from utils.module_rest import *
from behave import given, when, then
import json

@when(u'I send {method} items request to delete an item')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    #print ("rootId",context.response)
    generateFileJson("data/", "Item_DELETEDeleteIdItem", context.response.json())

@then(u'I receive {parameter_del} parameter {boolean}')
def step_impl(context,parameter_del,boolean):
    result = context.response.json()
    #print ("boo",result[parameter_del])
    expect(bool(boolean)).to_equal(result[parameter_del])