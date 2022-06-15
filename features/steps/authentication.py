import os
from base64 import b64encode

import requests
from behave import *
from dotenv import load_dotenv

load_dotenv()

TOKEN_KEY = os.getenv('TOKEN_KEY')
USERNAME_VALID = os.getenv('USERNAME_VALID')
PASSWORD_VALID = os.getenv('PASSWORD_VALID')
PASSWORD_INVALID = os.getenv('PASSWORD_INVALID')
URL = f"https://api.ona.io/api/v1/projects?owner={USERNAME_VALID}"


def basicHeader(username, password):
    return "Basic " + b64encode(f"{username}:{password}".encode()).decode("ascii")


@given(u'we are not authenticated')
def we_are_not_authenticated(context):
    context.headers = {}


@given(u'we authenticate using an invalid key')
def we_authenticate_using_an_invalid_key(context):
    if ('headers' not in context):
        context.headers = {}
    WRONG_TOKEN_KEY = "000009999922223444444"
    context.headers["Authorization"] = f"Token {WRONG_TOKEN_KEY}"


@given(u'we authenticate using a valid username/password')
def we_authenticate_using_a_valid_username_password(context):
    if ('headers' not in context):
        context.headers = {}
    context.headers["Authorization"] = basicHeader(USERNAME_VALID, PASSWORD_VALID)


@given(u'we authenticate using a bad username/password')
def we_authenticate_using_a_bad_username_password(context):
    if ('headers' not in context):
        context.headers = {}
    context.headers["Authorization"] = basicHeader(USERNAME_VALID, PASSWORD_INVALID)


@when(u'we request our list of projects')
def we_request_our_list_of_projects(context):
    context.response = requests.get(url=URL, headers=context.headers)


@then('we shall received a {status_code} status code')
def we_shall_received_a_XXX_status_code(context, status_code: int):
    assert context.response is not None
    assert context.response.status_code == int(status_code)


@then(u'the project list will be empty')
def the_project_list_will_be_empty(context):
    assert context.response is not None
    projects = context.response.json()
    assert len(projects) == 0


@then(u'the project list will not be empty')
def the_project_list_will_not_be_empty(context):
    assert context.response is not None
    projects = context.response.json()

    assert len(projects) > 0
