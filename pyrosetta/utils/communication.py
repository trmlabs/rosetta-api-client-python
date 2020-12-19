import requests

def post_request(url, data):
    return requests.post(url, data=data)