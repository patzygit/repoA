from compare import *
from utils.module_rest import *
from jsondiff import diff
from behave import given, when, then
import jsondiff
import json


@given(u'I have a pyloadBody')
def step_impl(context):
    context.pyloadBody = json.loads(context.text)
    print("*** ", context.text)

@when(u'I send {postmethod} items request to add a new item')
def step_impl(context,postmethod):
    context.method   = postmethod
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.pyloadrequest = context.pyloadBody
    context.response = perform_request(context.method, context.url, context.headers, context.pyloadrequest)
    generateFileJson("data/", "dataAddItem", context.response.json())

@then(u'I got response body of new item')
def step_impl(context):
    pass