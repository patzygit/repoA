from compare import *
from utils.module_rest import *
from behave import given, when, then


@given(u'I have a service with the id "{serviceMethod1}"')
def step_impl(context, serviceMethod1):
    context.serviceMethod1 = serviceMethod1

@when(u'I send "{method1}" filter by id request to have the result')
def step_impl(context, method1):
    context.method1  = method1
    url              = context.host + context.rootPath + context.serviceMethod1
    headers          = context.token
    context.response = perform_request(context.method1, url, headers)
    generateFileJson("data/", "data_filter_by_id", context.response.json())

@then(u'I receive the status code "{code}" of the response')
def step_impl(context, code):
    expect(context.response.status_code).to_equal(int(code))