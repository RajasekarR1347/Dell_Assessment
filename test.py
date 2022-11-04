from datetime import datetime
import requests
import pytest
import time

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



