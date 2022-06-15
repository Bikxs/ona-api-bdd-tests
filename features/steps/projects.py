import os
from pprint import pprint
from random import randint

import requests
from behave import *
from dotenv import load_dotenv

load_dotenv()

USERNAME_VALID = os.getenv('USERNAME_VALID')
TEST_PROJECT_ID = int(os.getenv('TEST_PROJECT_ID'))


@when('we request a list of projects')
def we_request_a_list_of_projects(context):
    URL = f"https://api.ona.io/api/v1/projects?owner={USERNAME_VALID}"
    context.response = requests.get(url=URL, headers=context.headers)


@when('we request for the test project')
def we_request_for_the_test_project(context):
    URL = f"https://api.ona.io/api/v1/projects/{TEST_PROJECT_ID}"
    context.response = requests.get(url=URL, headers=context.headers)


@when('we change the test project name')
def we_change_the_test_project_name(context):
    URL = f"https://api.ona.io/api/v1/projects/{TEST_PROJECT_ID}"
    randNumber = randint(1, 100_000)
    context.new_name = f'Test Project (#{randNumber})'
    data = {'name': context.new_name}
    context.response = requests.patch(url=URL, data=data, headers=context.headers)




@then('we get the list of projects with test project included')
def we_get_the_list_of_projects_we_defined_back(context):
    assert context.response is not None
    assert context.response.status_code == 200
    projects = context.response.json()
    assert len(projects) >= 1

    project_ids = {project["projectid"] for project in projects}
    # pprint(project_ids)
    assert TEST_PROJECT_ID in project_ids


@then('we get the test project back')
def we_get_the_test_project_back(context):
    assert context.response is not None
    assert context.response.status_code == 200
    project = context.response.json()
    assert project["projectid"] == TEST_PROJECT_ID


@then('we get test project with new name')
def we_get_test_project_with_new_name(context):
    URL = f"https://api.ona.io/api/v1/projects/{TEST_PROJECT_ID}"
    context.response = requests.get(url=URL, headers=context.headers)
    assert context.new_name == context.response.json()['name']
    # reset the project name back to Testing Project
    data = {'name': 'Testing Project'}
    context.response = requests.patch(url=URL, data=data, headers=context.headers)
    project = context.response.json()
    print("Test Project")
    pprint(project)
