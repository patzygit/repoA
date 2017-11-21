import requests
import json

def perform_get_request(host, headers=None):
    r = requests.get(host, headers=headers)
    return r.json()

def perform_request(method, endpoint, body='', headers=''):
    if method == 'GET':
	    result = requests.get(endpoint, headers=headers)
    if method == 'POST':
	    result = requests.post(endpoint, payload=body, headers=headers)
    if method == 'PUT':
        result = requests.put(endpoint, payload=body, headers=headers)
    if method == 'DELETE':
        result = requests.delete(endpoint, headers=headers)
    return result

def generateFileJson(path, fileName, data):
    filePathNameWExt = path + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)