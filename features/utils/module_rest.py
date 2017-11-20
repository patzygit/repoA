import requests
import json

def perform_get_request(host,headers=None):
       r = requests.get(host,headers=headers)
       return r.json()

def perform_request(method, endpoint,body=None,headers=None):
	##enpoint shoudl eb already completed
    if method == 'GET':
	    result= requests.get(endpoint,headers)
    elif method == 'POST':
	    result= requests.post(endpoint, payload=body, headers=headers)

    return result

def add_headers(host):
    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
