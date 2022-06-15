import os

from behave import *
from dotenv import load_dotenv

load_dotenv()
TOKEN_KEY = os.getenv('TOKEN_KEY')


@given(u'we authenticate using a valid key')
def we_authenticate_using_a_valid_key(context):
    if ('headers' not in context):
        context.headers = {}
    context.headers["Authorization"] = f"Token {TOKEN_KEY}"
