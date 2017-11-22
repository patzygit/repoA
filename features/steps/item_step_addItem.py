from compare import *
from utils.module_rest import *
#from jsondiff import diff
from behave import given, when, then

@when(u'I send POST items request to add a new item')
def step_impl(context,postmethod):
    context.method   = postmethod
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers, context.pyloadRequest)
    generateFileJson("data/", "dataAddItems", context.response.json())

@when(u'I have a pyloadBody')
def step_impl(context):
    #context.pyloadRequest = json.loads(context.text)
    print("*** ",context.text)

@then(u'I got response body of new item')
def step_impl(context):
    pass