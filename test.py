import json
from datetime import datetime
import requests
import pytest
import time
from cerberus import Validator
from schema import schemas

url = requests.get("https://swapi.py4e.com/api/people/")
number_0 = requests.get("https://swapi.py4e.com/api/people/0")
js_response = url.json()

people=[]

def get_time(func):
    def inner(*args):
        start  = time.time()
        print(func.__name__, 'start time', datetime.datetime.utcfromtimestamp(start))
        a=func(*args)
        end = time.time()
        print(func.__name__, 'start time', datetime.datetime.utcfromtimestamp(end))
        time_diff = datetime.datetime.utcfromtimestamp(end - start)
        print(func.__name__,"time diff",time_diff.strftime('%H:%M:%S:%f'))
        return a
    return inner

#⦁	create fixture that returns an array with all people
@pytest.fixture()
def test_get_user():
    for user in js_response['results']:
      tot_user = user['name']
      people.append(tot_user)
    return people

@get_time
def test_read_one_operation_has_expected_schema():
   response = requests.get(f'{}/1')
   person = json.loads(response.text)

def unique_names(l):
    return list(set([x for x in l if l.count(x) > 1]))

#create test which checks that names of all people are unique

def test_unique_names(test_get_user):
    if unique_names(people)==[]:
        print("no duplicate")

#⦁	create test (or a few) with validation that search for people is case insensitive
def test_case_insensitive(test_get_user):
    assert people[0]

# create test which validates that there is no page with number 0 for people request
def test_page_number_0():
    url1 = number_0
    status=url1.status_code
    assert status == 404

'''
⦁	create test(s) which validate that all people objects contain required schema fields.
If validation fails – person id and name should be in error/fail message.
All persons with failed validation must be reported during one test run.
⦁	create factory fixture “search_in_resource” that returns search function depending on the resource name provided as a parameter (people, planet, etc)
⦁	create test which checks that search for any char in English alphabet or any number from 0 to 9 returns number of results>0 except cases of search by 6, 9 and 0. It is not allowed to use loops inside the test body.


'''


