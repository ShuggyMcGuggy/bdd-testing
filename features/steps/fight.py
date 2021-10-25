from behave import *

@given('the ninja has a third level black-belt')
def step_impl(context):
    pass

@when('attacked by a samurai')
def step_impl(context):
    assert True is not False
    
@then('the ninja should engage the opponent')
def step_impl(context):
    assert context.failed is False     

@when('attacked by Chuck Norris')
def step_impl(context):
    assert True is not False
    
@then('the ninja should run for his life')
def step_impl(context):
    assert context.failed is False  
