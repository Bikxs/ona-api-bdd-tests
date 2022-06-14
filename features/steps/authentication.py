from behave import *
from requests.auth import HTTPBasicAuth
import requests
import os
from dotenv import load_dotenv
load_dotenv()


response = None
URL = "https://api.ona.io/api/v1/"
TOKEN_KEY = os.getenv('TOKEN_KEY') #"5ebc126785982c33ef0cffee76a50d40f7e47b8d"
USERNAME_VALID = os.getenv('USERNAME_VALID') # "bikxs"
PASSWORD_VALID = os.getenv('PASSWORD_VALID') # "Crystals."
PASSWORD_INVALID = os.getenv('PASSWORD_INVALID') # "35734633!"



@given(u'we are not authenticated')
def we_are_not_authenticated(context):
    global response
    response = None


@when(u'we authenticate using a valid key')
def we_authenticate_using_a_valid_key(context):
    global response

    headers = {"Authorization": f"Token {TOKEN_KEY}"}
    response = requests.get(url=URL, headers=headers)


@when(u'we authenticate using an invalid key')
def we_authenticate_using_an_invalid_key(context):
    global response
    global response

    TOKEN_KEY = "000009999922223444444"
    headers = {"Authorization": f"Token {TOKEN_KEY}"}
    response = requests.get(url=URL, headers=headers)

@when(u'we authenticate using a valid username/password')
def we_authenticate_using_a_valid_username_password(context):
    global response

    response = requests.get(url=URL, auth=HTTPBasicAuth(USERNAME_VALID, PASSWORD_VALID))


@when(u'we authenticate using a bad username/password')
def we_authenticate_using_a_bad_username_password(context):
    global response

    response = requests.get(url=URL, auth=HTTPBasicAuth(USERNAME_VALID, PASSWORD_INVALID))

@then(u'we shall received a 200 status code')
def we_shall_received_a_200_status_code(context):
    global response
    assert response is not None
    assert response.status_code == 200

@then(u'we shall received a 401 status code')
def we_shall_received_a_401_status_code(context):
    global response
    assert response is not None
    print(f"response.status_code = {response.status_code}")
    assert response.status_code == 401
