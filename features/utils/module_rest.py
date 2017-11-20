import requests
import json

def perform_get_request(host, hearders=None):
     r = requests.get(host, hearder=hearders)
     return  r.json()


def perform_request(method, endpoint):
    if  method == 'GET':
        requests.get(endpoint)
    if  method == 'POST':
        requests.post()



