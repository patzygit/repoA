from compare import expect

@given(u'I have a username "{username}"')
def step_impl(context, username):
    context.username = username
    print(context.username)
    expect(context.username).to_equal(username)



@given(u'I have a token "{token}"')
def step_impl(context, token):
    context.token = token
    print(context.token)
    expect(context.token).to_equal(token)

@when(u'I GET  my request to success')
def step_impl(context):
    pass


@then(u'I receive status code {response} for the response')
def step_impl(context, response):
    context.response = response
    print(context.response)
    expect(context.response).to_equal(int(response))