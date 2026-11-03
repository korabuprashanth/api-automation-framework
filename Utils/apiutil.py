import json,requests

def get_API_request(url,op_headers=None):
    headers={'accept':'application/json'}
    headers=headers|op_headers if isinstance(op_headers,dict) else headers
    resp=requests.get(url, headers=headers)
    return resp

def post_API_request(url,body,op_headers=None):
    headers={'accept':'application/json'}
    if isinstance(op_headers,dict):
        headers=headers|op_headers
    else:
        headers
    resp=requests.post(url,json=body, headers=headers)
    return resp

def delete_API_data(url,op_headers=None):
    headers={'accept':'application/json'}
    headers = headers | op_headers if isinstance(op_headers, dict) else headers
    response=requests.delete(url,headers=headers)
    return response

def patch_API_data(url,body,op_headers=None):
    headers={'accept':'application/json'}
    headers = headers | op_headers if isinstance(op_headers, dict) else headers
    response=requests.patch(url,json=body,headers=headers)
    return response

def post_API_request_files(url, data=None, files=None, op_headers=None):
    """
    POST request for file uploads (multipart/form-data)
    """
    headers = {'accept': 'application/json'}
    if isinstance(op_headers, dict):
        headers = headers | op_headers

    resp = requests.post(url, data=data, files=files, headers=headers)
    return resp
