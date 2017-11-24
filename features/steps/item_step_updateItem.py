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
    generateFileJson("data/", "Item_PUTUpdateItem", context.response.json())


@then(u'I recieve {updatedParameter} parameter for item with {description}')
def step_impl(context, updatedParameter, description):
    print("upParameter",updatedParameter)
    print("description",description)
    result = context.response.json()
    print("result",result[updatedParameter])
    expect(str(description)).to_equal(result[updatedParameter])