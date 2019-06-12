#!/usr/bin/env python3

"""
pip3 install requests argparse time
"""

import requests,argparse,time
from f5functions import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cmdargs = argparse.ArgumentParser()

cmdargs.add_argument('--bigip', action='store', required=True, type=str,help='management IP for reaching the BIG-IP REST interface')
cmdargs.add_argument('--bigip_port', action='store', required=False, type=int,help='port for reaching the BIG-IP REST interface', default=443)
cmdargs.add_argument('--username', action='store', required=True, type=str, help='username for the BIG-IP')
cmdargs.add_argument('--password', action='store', required=True, type=str, help='password for the BIG-IP')
cmdargs.add_argument('--partitions', nargs='+', required=True, type=str, help='list of partitions separated by spaces')

parsed_args = cmdargs.parse_args()

bigip = parsed_args.bigip
bigip_port = parsed_args.bigip_port
username = parsed_args.username
password = parsed_args.password
partitions = parsed_args.partitions

def kube_polling_simulation(target_partition):
    print('Polling partition ' + target_partition)
    start_time = time.perf_counter()
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/auth/partition/' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/monitor/http/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/monitor/https/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/monitor/tcp/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/monitor/udp/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/monitor/gateway-icmp/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/sys/application/service/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/node/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/virtual-address/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/rule/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/data-group/internal/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/virtual/?$filter=partition+eq+' + target_partition + '&expandSubcollections=true')
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/pool/?$filter=partition+eq+' + target_partition + '&expandSubcollections=true')
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/policy/?$filter=partition+eq+' + target_partition + '&expandSubcollections=true')
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/profile/client-ssl/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/sys/file/ssl-cert/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/sys/file/ssl-key/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/ltm/profile/server-ssl/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    task_start_time = time.perf_counter()
    apiResponse = icontrol_get(bigip, username, password, '/sys/file/ssl-cert/?$filter=partition+eq+' + target_partition)
    print('Finished task in ' + str(time.perf_counter() - task_start_time) + ' - ' + str(apiResponse.text[0:150]))
    if apiResponse.status_code != 200:
        print(apiResponse.text)
    apiResponse = icontrol_get(bigip, username, password, '/sys/file/ssl-key/?$filter=partition+eq+' + target_partition)
    time_to_completion = time.perf_counter() - start_time
    print('Polled partition ' + target_partition + ' in ' + str(time_to_completion) + ' seconds')

if __name__ == '__main__':
    for partition in partitions:
        kube_polling_simulation(partition)
