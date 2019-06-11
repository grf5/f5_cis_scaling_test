#!/usr/bin/env python3

import json,sys,requests

def abort_script(reason):
    print('*** Aborting script execution! ***')
    if len(str(reason)) > 0:
        print('ERROR: ' + str(reason))
    sys.exit(2)

def icontrol_get(host,username,password,path):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.get(apiUri,verify=False)
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)

def icontrol_post(host,username,password,path,api_payload):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.post(apiUri,verify=False,data=json.dumps(api_payload))
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)

def icontrol_put(host,username,password,path,api_payload):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.put(apiUri,verify=False,data=json.dumps(api_payload))
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)

def icontrol_patch(host,username,password,path,api_payload):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path
    try:
        apiResponse = apiCall.patch(apiUri,verify=False,data=json.dumps(api_payload))
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)

def icontrol_delete(host,username,password,path,object):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm' + path + object
    try:
        apiResponse = apiCall.delete(apiUri,verify=False)
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)

def icontrol_test_connection(host,username,password):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm/sys/clock'
    try:
        apiResponse = apiCall.get(apiUri,verify=False)
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    if '"kind"' in apiResponse.text:
        testresult = True
    else:
        testresult = False
    return(testresult)

def icontrol_save_config(host,username,password):
    apiCall = requests.session()
    apiCall.headers.update({'Content-type':'application/json'})
    apiCall.auth = (username,password)
    apiUri = 'https://' + host + '/mgmt/tm/sys/config'
    try:
        apiResponse = apiCall.post(apiUri,verify=False,data=json.dumps({'command':'save'}))
    except requests.exceptions.RequestException as e:
        abort_script(str(e))
    return(apiResponse)