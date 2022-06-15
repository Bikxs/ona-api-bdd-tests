# ONA-API BDD Tests

Python behave tests to test ONA-API

Ona JSON Rest Api Endpoints being tested are available here [ONAAPI](https://api.ona.io/api)

If you don't have an account use this link to create a free account [Register](http://ona.io/login) and request for your API-KEY in the [profile->settings](https://ona.io/bikxs/settings#/s/api) page. 



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements listed in requirements.md.

```bash
pip install -r requirements.txt
```

## Usage
### Add credentials to environment
Copy over the .env_sample to .env and populate the required creditions, project and formids.

If you do not know what is your projectId or formId use the provided python script to list them. 
```bash
python3 getProjectsIDAndFormsIDs.py
```
You will need to have created one project and added a form before running the test scripts

### run the test scripts
The tests have been defined using gherkin and behave. To execute them run the behave (intalled by pip) command
```bash
behave
```
A convinience script that runs all the tests and create friendly junit reports has also been included
```bash
python3 testAll.py.py
```

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40bikxs)](https://twitter.com/BikoNyamai)