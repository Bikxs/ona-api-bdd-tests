from base64 import b64encode
from pprint import pprint

import requests


def basicHeader(username, password):
    return "Basic " + b64encode(f"{username}:{password}".encode()).decode("ascii")


if __name__ == '__main__':
    print("This script will retrieve a listing of your projects \nand forms with their IDs from ONA")
    username = input("Please enter your ONA credentials:\n\tusername:")
    username = username.strip()
    if username == "":
        print("Exiting...")
        exit(0)
    password = input("\tpassword: ")
    if password.strip() == "":
        print("Exiting...")
        exit(0)

    headers = {"Authorization": basicHeader(username,password)}
    URL = f"https://api.ona.io/api/v1/projects?owner={username}"
    response = requests.get(url=URL, headers=headers)
    if(response.status_code==200):
        print()
        print()
        projects = response.json()
        if(projects):
            print("*" * 50)
            print("Projects")
            for project in projects:
                print("-" * 50)
                print(f"\tprojectId: {project['projectid']} = {project['name']}")
                for form in project['forms']:
                    print(f"\t\tformId: {form['formid']} = {form['name']}")
            print("*" * 50)
            print()
            print("Select One projectId and a formId from above and populate them into your .env file")
            print("DANGER: NOTE THAT THE PROJECT NAME AND FORM NAME SELECTED WILL BE CHANGED!!!")
        else:
            print("You do not have projects defined in your acccount - please create one")
    else:
        print("Invalid username or password")
