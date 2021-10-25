from behave import *

@given('we have behave installed')
def step_impl(context):
    #pass
    assert context.failed is False

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
    
@given ('We load a specified spreadsheet')
def step_impl(context):
    assert 2==1,"Makes no Sense"
    
@when('We check the column headings')
def step_impl(context):
    fail
    
@then('We will report an error with enough test to ideintify the problem')   
def step_impl(context):    
    assert True is not False
    
