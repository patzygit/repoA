from compare import *
from utils.module_rest import *
from behave import given, when, then

@given(u'I have a service with id of the item "{serviceMethod2}"')
def step_impl(context, serviceMethod2):
    context.serviceMethod2 = serviceMethod2

@when(u'I send "{method2}" filter by the id of the item and get the result')
def step_impl(context, method2):
    context.method2 = method2
    url = context.host + context.rootPath + context.serviceMethod2
    headers = context.token
    context.response = perform_request(context.method2, url, headers)
    generateFileJson("data/", "data_item_one_filter", context.response.json())

@then(u'I receive the status code "{code2}"')
def step_impl(context, code2):
    expect(context.response.status_code).to_equal(int(code2))