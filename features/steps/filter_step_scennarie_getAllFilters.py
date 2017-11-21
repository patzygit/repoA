from compare import *
from utils.module_rest import *
from behave import given, when, then

@given(u'I have a new user authenticated')
def step_impl(context):
    pass

@given(u'I have a service of "{servicemethod}"')
def step_impl(context, servicemethod):
    context.servicemethod = servicemethod

@when(u'I send "{method}" filters request, the result is returned.')
def step_impl(context, method):
    context.method   = method
    context.url      = context.host + context.rootPath + context.servicemethod
    context.headers  = context.token
    context.response = perform_request(context.method, context.url, context.headers)
    generateFileJson("data/", "data_all_filters", context.response.json())

@then(u'I receive the status code "{status_code}" for the response')
def step_impl(context, status_code):
    expect(context.response.status_code).to_equal(int(status_code))