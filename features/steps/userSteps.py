from compare import *
from utils.module_rest import *

@given(u'I have a user authenticated')
def step_impl(context):
    pass

@given(u'I have service for "{serviceMethod}"')
def step_impl(context, serviceMethod ):
    context.serviceMethod = serviceMethod

@when(u'I send {method} user request to have user information')
def step_impl(context, method):
    context.method = method
    url = context.host + context.rootPath + context.serviceMethod
    headers = context.token
    context.response = perform_request(context.method, url, headers)

    print(context.response.json())
    generateFileJson("data/", "data_user", context.response.json())

@then(u'I receive status code {status_code} for the response')
def step_impl(context, status_code):
    expect(int(status_code)).to_equal(context.response.status_code)
