import requests
import json

def http_get(url, params = None):
    if params is None:
        r = requests.get(url)
    else:
        r = requests.get(url, params = params)
    data = json.loads(r.text)
    return data, r.status_code

def http_post(url, data, headers = None): 
    data=json.dumps(data)
    if headers is None:
        req = requests.post(url, data)      
    else:
        req = requests.post(url, data, headers = headers)
    response = req.text   
    r = json.loads(response)
    return r

def http_put(url,data):
    if data is None:
        r=requests.put(url)
    else:
        r=requests.put(url,data=data)
    data=json.loads(r.text)
    return data,r.status_code

def http_delete(url,iid):
    r=requests.delete(url+'/'+iid)
    return r.status_code
