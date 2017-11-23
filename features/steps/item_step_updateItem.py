from compare import *
from utils.module_rest import *
from behave import given, when, then
import json

@given(u'I have a updateBody')
def step_impl(context):
    context.updateToBody = json.loads(context.text)


@when(u'I send {putmethod} items request to update a new item')
def step_impl(context, putmethod):
    context.method  = putmethod
    context.url     = context.host + context.rootPath + context.servicemethod
    context.headers = context.token
    context.pyloadrequest = context.updateToBody
    context.response = perform_request(context.method, context.url, context.headers, context.pyloadrequest)
    generateFileJson("data/", "dataUpdateItem", context.response.json())