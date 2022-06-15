import os
from pprint import pprint
from random import randint

import requests
from behave import *
from dotenv import load_dotenv

load_dotenv()

USERNAME_VALID = os.getenv('USERNAME_VALID')
TEST_PROJECT_ID = int(os.getenv('TEST_PROJECT_ID'))
TEST_FORM_ID = int(os.getenv('TEST_FORM_ID'))


@when(u'we request a list of test project forms')
def we_request_a_list_of_test_project_forms(context):
    URL = f"https://api.ona.io/api/v1/forms?owner={USERNAME_VALID}"
    context.response = requests.get(url=URL, headers=context.headers)


@when(u'we request a infomation of test form')
def we_request_a_infomation_of_test_form(context):
    URL = f"https://api.ona.io/api/v1/forms/{TEST_FORM_ID}"
    context.response = requests.get(url=URL, headers=context.headers)


@when(u'we change information of test form')
def we_change_information_of_test_form(context):
    URL = f"https://api.ona.io/api/v1/forms/{TEST_FORM_ID}"
    randNumber = randint(1, 100_000)
    context.new_title = f'Test Form (#{randNumber})'
    data = {'title': context.new_title}
    context.response = requests.patch(url=URL, data=data, headers=context.headers)


@then(u'we get a list of project forms')
def we_should_get_a_list_of_forms_it_included(context):
    assert context.response is not None
    assert context.response.status_code == 200


@then(u'the test form id should be included in the list')
def the_test_form_id_should_be_included_in_the_list(context):
    forms = context.response.json()
    formids = {form['formid'] for form in forms}
    assert TEST_FORM_ID in formids


@then(u'we should get infomation about the test form')
def we_should_get_infomation_about_the_test_form(context):
    assert context.response is not None
    assert context.response.status_code == 200
    form = context.response.json()
    assert TEST_FORM_ID == form['formid']


@then(u'we should get updated infomation about the test form')
def step_impl(context):
    URL = f"https://api.ona.io/api/v1/forms/{TEST_FORM_ID}"
    context.response = requests.get(url=URL, headers=context.headers)
    form = context.response.json()
    # print(context.new_title)
    # print(form['title'])
    assert context.new_title == form['title']
    data = {'title': 'Test Form'}
    context.response = requests.patch(url=URL, data=data, headers=context.headers)
    form = context.response.json()
    print("Test form")
    pprint(form)