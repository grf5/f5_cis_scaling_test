#!/usr/bin/env python3

"""
pip3 install --upgrade pip argparse json requests sys
"""

import argparse, json, requests, sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from f5functions import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cmdargs = argparse.ArgumentParser()

cmdargs.add_argument('--bigip', action='store', required=True, type=str,help='management IP for reaching the BIG-IP REST interface')
cmdargs.add_argument('--bigip_port', action='store', required=False, type=int,help='port for reaching the BIG-IP REST interface', default=443)
cmdargs.add_argument('--username', action='store', required=True, type=str, help='username for the BIG-IP')
cmdargs.add_argument('--password', action='store', required=True, type=str, help='password for the BIG-IP')
cmdargs.add_argument('--partitioncount', action='store', required=False, type=int,help='total number of partitions to create (defaults to 10)', default=10)
cmdargs.add_argument('--partitionbase', action='store', required=False, type=int,help='first partition id (defaults to 1)', default=1)
cmdargs.add_argument('--partitionprefix', action='store', required=False, type=str,help='prefix for partition names (defaults to partition-)', default='partition-')
cmdargs.add_argument('--virtualcount', action='store', required=False, type=int,help='total number of partitions to create (defaults to 10)', default=10)
cmdargs.add_argument('--virtualaddressprefix', action='store', required=False, type=str,help='first two octets of virtual addresses (defaults to 172.16.)', default='172.16.')
cmdargs.add_argument('--virtualaddressbase', action='store', required=False, type=str,help='starting value of host address octet (defaults to 1)', default=1)
cmdargs.add_argument('--virtualprefix', action='store', required=False, type=str,help='prefix for virtual server names (defaults to virtual-)', default='virtual-')
cmdargs.add_argument('--virtualportbase', action='store', required=False, type=int,help='port for virtual server (defaults to 443)', default=443)
cmdargs.add_argument('--virtualincrementport', action='store_false', required=False,help='flag to increment pool member port number (off by default)')
cmdargs.add_argument('--virtualincrementaddress', action='store_true', required=False,help='flag to increment pool member ip address (on by default)')
cmdargs.add_argument('--poolprefix', action='store', required=False, type=str,help='pool name prefix (defaults to pool-)', default='pool-')
cmdargs.add_argument('--poolmembercount', action='store', required=False, type=int,help='pool member count (defaults to 50)', default=50)
cmdargs.add_argument('--poolmemberprefix', action='store', required=False, type=str,help='pool member name prefix (defaults to poolmember-)', default='poolmember-')
cmdargs.add_argument('--poolmonitorprefix', action='store', required=False, type=str,help='pool monitor name prefix (defaults to poolmonitor-)', default='poolmonitor-')
cmdargs.add_argument('--poolmonitortype', action='store', required=False, type=str,help='pool monitor type [http | gateway-icmp ] (defaults to http)', default='http')
cmdargs.add_argument('--poolmemberaddressprefix', action='store', required=False, type=str,help='first octet of pool member addresses (defaults to 10.)', default='10.')
cmdargs.add_argument('--poolmemberaddressbase', action='store', required=False, type=int,help='first host octet of pool member addresses (defaults to 1)', default=1)
cmdargs.add_argument('--poolmemberportbase', action='store', required=False, type=int,help='port for pool members (defaults to 443)', default=443)
cmdargs.add_argument('--poolmemberincrementport', action='store_true', required=False,help='flag to increment pool member port number (off by default)')
cmdargs.add_argument('--poolmemberincrementaddress', action='store_false', required=False,help='flag to increment pool member ip address (on by default)')
cmdargs.add_argument('--delete', action='store_true', required=False,help='flag used to delete a previous configuration - use the exact cli args as the build!')

parsed_args = cmdargs.parse_args()

bigip = parsed_args.bigip
bigip_port = parsed_args.bigip_port
username = parsed_args.username
password = parsed_args.password
partitioncount = parsed_args.partitioncount
partitionbase = parsed_args.partitionbase
partitionprefix = parsed_args.partitionprefix
virtualcount = parsed_args.virtualcount
virtualaddressprefix = parsed_args.virtualaddressprefix
virtualaddressbase = parsed_args.virtualaddressbase
virtualprefix = parsed_args.virtualprefix
virtualportbase = parsed_args.virtualportbase
virtualincrementport = parsed_args.virtualincrementport
virtualincrementaddress = parsed_args.virtualincrementaddress
poolprefix = parsed_args.poolprefix
poolmembercount = parsed_args.poolmembercount
poolmemberprefix = parsed_args.poolmemberprefix
poolmonitorprefix = parsed_args.poolmonitorprefix
poolmonitortype = parsed_args.poolmonitortype
poolmemberaddressprefix = parsed_args.poolmemberaddressprefix
poolmemberaddressbase = parsed_args.poolmemberaddressbase
poolmemberportbase = parsed_args.poolmemberportbase
poolmemberincrementport = parsed_args.poolmemberincrementport
poolmemberincrementaddress = parsed_args.poolmemberincrementaddress
deletemode = parsed_args.delete

partitions = []

for current_partition in range(partitionbase, partitioncount + 1):
    partitiondef = {}
    partitiondef['name'] = partitionprefix + str(current_partition)
    partitiondef['id'] = current_partition
    partitiondef['virtuals'] = []
    for current_virtual in range(1, virtualcount + 1):
        virtualdef = {}
        virtualdef['name'] = virtualprefix + str(current_virtual)
        if virtualincrementaddress == True:
            current_virtual_address = virtualaddressprefix + str(current_partition) + '.' + str(virtualaddressbase + current_virtual - 1)
        else:
            current_virtual_address = virtualaddressprefix + str(current_partition) + '.' + str(virtualaddressbase)
        if virtualincrementport == True:
            current_virtual_port = str(virtualportbase + current_virtual - 1)
        else:
            current_virtual_port = str(virtualportbase)
        virtualdef['destination'] = current_virtual_address + ':' + current_virtual_port
        virtualdef['partition'] = partitiondef['name']
        virtualdef['sourceAddressTranslation'] = {'type': 'automap'}
        pooldef = {}
        pooldef['name'] = poolprefix + str(current_virtual)
        pooldef['partition'] = partitiondef['name']
        pooldef['monitor'] = poolmonitorprefix + str(current_virtual)
        pooldef['members'] = []
        pooldef['nodes'] = []
        for current_member in range(1, poolmembercount + 1):
            if poolmemberincrementaddress == True:
                current_pool_member_address = poolmemberaddressprefix + str(current_partition) + '.' + str(current_partition) + '.' + str(poolmemberaddressbase + current_member - 1)
            elif poolmemberincrementaddress == False:
                current_pool_member_address = poolmemberaddressprefix + str(current_partition) + '.' + str(current_partition) + '.' + str(poolmemberaddressbase)
            if poolmemberincrementport == True:
                current_pool_member_port = str(poolmemberportbase + current_member - 1)
            elif poolmemberincrementport == False:
                current_pool_member_port = str(poolmemberportbase)
            current_pool_member = current_pool_member_address + ':' + current_pool_member_port + str(current_partition) + str(current_virtual)
            pooldef['members'].append(current_pool_member)
            pooldef['nodes'].append(current_pool_member_address)
        virtualdef['pool'] = pooldef
        partitiondef['virtuals'].append(virtualdef)
    partitions.append(partitiondef)

if __name__ == "__main__":
    connectivity = icontrol_test_connection(bigip, username, password)
    if connectivity == False:
        abort_script('Fatal error! Could not reach the BIG-IP iControl REST interface!')
    elif connectivity == True:
        print('Successfully connected to BIG-IP')
    if deletemode == False:
        for current_partition in partitions:
            api_payload = {}
            api_payload['name'] = current_partition['name']
            api_payload['id'] = current_partition['id']
            print('Creating partition ' + str(api_payload))
            api_response = icontrol_post(bigip, username, password, '/auth/partition', api_payload)
            if not api_response.ok:
                print(api_response.text)
            for current_virtual in current_partition['virtuals']:
                api_payload = {}
                api_payload['name'] = current_virtual['pool']['monitor']
                api_payload['partition'] = current_partition['name']
                print('Creating pool monitor ' + str(api_payload))
                api_response = icontrol_post(bigip, username, password, '/ltm/monitor/' + poolmonitortype, api_payload)
                if not api_response.ok:
                    print(api_response.text)
                api_payload = {}
                api_payload['name'] = current_virtual['pool']['name']
                api_payload['partition'] = current_partition['name']
                api_payload['monitor'] = current_virtual['pool']['monitor']
                api_payload['members'] = current_virtual['pool']['members']
                print('Creating pool ' + str(api_payload))
                api_response = icontrol_post(bigip, username, password, '/ltm/pool', api_payload)
                if not api_response.ok:
                    print(api_response.text)
                api_payload = {}
                api_payload['name'] = current_virtual['name']
                api_payload['partition'] = current_partition['name']
                api_payload['destination'] = current_virtual['destination']
                api_payload['sourceAddressTranslation'] = current_virtual['sourceAddressTranslation']
                print('Creating virtual ' + str(api_payload))
                api_response = icontrol_post(bigip, username, password, '/ltm/virtual', api_payload)
                if not api_response.ok:
                    print(api_response.text)
    elif deletemode == True:
        for current_partition in partitions:
            for current_virtual in current_partition['virtuals']:
                print('Deleting virtual ' + '/~' + current_partition['name'] + '~' + current_virtual['name'])
                api_response = icontrol_delete(bigip, username, password, '/ltm/virtual', '/~' + current_partition['name'] + '~' + current_virtual['name'])
                if not api_response.ok:
                    print(api_response)
                print('Deleting pool ' + '/~' + current_partition['name'] + '~' + current_virtual['pool']['name'])
                api_response = icontrol_delete(bigip, username, password, '/ltm/pool', '/~' + current_partition['name'] + '~' + current_virtual['pool']['name'])
                if not api_response.ok:
                    print(api_response)
                print('Deleting monitor ' + '/~' + current_partition['name'] + '~' + current_virtual['pool']['monitor'])
                api_response = icontrol_delete(bigip, username, password, '/ltm/monitor/' + poolmonitortype, '/~' + current_partition['name'] + '~' + current_virtual['pool']['monitor'])
                if not api_response.ok:
                    print(api_response)
                for current_node in current_virtual['pool']['nodes']:
                    print('Deleting node ' + '/~' + current_partition['name'] + '~' + current_node)
                    api_response = icontrol_delete(bigip, username, password, '/ltm/node', '/~' + current_partition['name'] + '~' + current_node)
                    if not api_response.ok:
                        print(api_response)
            print('Deleting partition ' + current_partition['name'])
            api_response = icontrol_delete(bigip, username, password, '/auth/partition/',  current_partition['name'])
            if not api_response.ok:
                print(api_response.text)
    icontrol_save_config(bigip, username, password)
