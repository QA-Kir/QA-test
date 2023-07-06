import requests
from config import *

def test_get_users(get_users):
    assert get_users.status_code == 200, 'Error: wrong status code'
    req = get_users.json()
    assert(req['data'][0]['last_name']) == 'Lawson'


def test_get_user():
    r = requests.get(url_update_user)
    assert r.status_code == 200
    req = r.json()
    assert(req['data']['first_name']) == 'Janet'

def test_post_user():
    r = requests.post(url=url_create_user,data=params_create_user)
    assert r.status_code == 201    

#Это для ДЗ
#1 case
def test_user_not_found():
    r = requests.get(url_single_user_not_found)
    assert r.status_code == 404
    req = r.json()
    assert(req) == {}

#2 case
def test_list_resource():
    r = requests.get(url_list_resource)
    assert r.status_code == 200
    req = r.json()
    assert (req['data'][2]['name']) == 'true red'

#3 case
def test_single_resource_not_found():
    r = requests.get(url_single_resource_404)
    assert r.status_code == 404
    req = r.json()
    assert (req) == {}   