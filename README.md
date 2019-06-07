# f5_cis_scaling_test

To create the configuration:
 
<pre>
usage: kube_scale_config.py [-h] --bigip BIGIP [--bigip_port BIGIP_PORT]
                            --username USERNAME --password PASSWORD
                            [--partitioncount PARTITIONCOUNT]
                            [--partitionbase PARTITIONBASE]
                            [--partitionprefix PARTITIONPREFIX]
                            [--virtualcount VIRTUALCOUNT]
                            [--virtualaddressprefix VIRTUALADDRESSPREFIX]
                            [--virtualaddressbase VIRTUALADDRESSBASE]
                            [--virtualprefix VIRTUALPREFIX]
                            [--virtualportbase VIRTUALPORTBASE]
                            [--virtualincrementport]
                            [--virtualincrementaddress]
                            [--poolprefix POOLPREFIX]
                            [--poolmembercount POOLMEMBERCOUNT]
                            [--poolmemberprefix POOLMEMBERPREFIX]
                            [--poolmonitorprefix POOLMONITORPREFIX]
                            [--poolmonitortype POOLMONITORTYPE]
                            [--poolmemberaddressprefix POOLMEMBERADDRESSPREFIX]
                            [--poolmemberaddressbase POOLMEMBERADDRESSBASE]
                            [--poolmemberportbase POOLMEMBERPORTBASE]
                            [--poolmemberincrementport]
                            [--poolmemberincrementaddress] [--delete]

optional arguments:
  -h, --help            show this help message and exit
  --bigip BIGIP         management IP for reaching the BIG-IP REST interface
  --bigip_port BIGIP_PORT
                        port for reaching the BIG-IP REST interface
  --username USERNAME   username for the BIG-IP
  --password PASSWORD   password for the BIG-IP
  --partitioncount PARTITIONCOUNT
                        total number of partitions to create (defaults to 10)
  --partitionbase PARTITIONBASE
                        first partition id (defaults to 1)
  --partitionprefix PARTITIONPREFIX
                        prefix for partition names (defaults to partition-)
  --virtualcount VIRTUALCOUNT
                        total number of partitions to create (defaults to 10)
  --virtualaddressprefix VIRTUALADDRESSPREFIX
                        first two octets of virtual addresses (defaults to
                        172.16.)
  --virtualaddressbase VIRTUALADDRESSBASE
                        starting value of host address octet (defaults to 1)
  --virtualprefix VIRTUALPREFIX
                        prefix for virtual server names (defaults to virtual-)
  --virtualportbase VIRTUALPORTBASE
                        port for virtual server (defaults to 443)
  --virtualincrementport
                        flag to increment pool member port number (off by
                        default)
  --virtualincrementaddress
                        flag to increment pool member ip address (on by
                        default)
  --poolprefix POOLPREFIX
                        pool name prefix (defaults to pool-)
  --poolmembercount POOLMEMBERCOUNT
                        pool member count (defaults to 50)
  --poolmemberprefix POOLMEMBERPREFIX
                        pool member name prefix (defaults to poolmember-)
  --poolmonitorprefix POOLMONITORPREFIX
                        pool monitor name prefix (defaults to poolmonitor-)
  --poolmonitortype POOLMONITORTYPE
                        pool monitor type [http | gateway-icmp ] (defaults to
                        http)
  --poolmemberaddressprefix POOLMEMBERADDRESSPREFIX
                        first octet of pool member addresses (defaults to 10.)
  --poolmemberaddressbase POOLMEMBERADDRESSBASE
                        first host octet of pool member addresses (defaults to
                        1)
  --poolmemberportbase POOLMEMBERPORTBASE
                        port for pool members (defaults to 443)
  --poolmemberincrementport
                        flag to increment pool member port number (off by
                        default)
  --poolmemberincrementaddress
                        flag to increment pool member ip address (on by
                        default)
  --delete              flag used to delete a previous configuration - use the
                        exact cli args as the build!
</pre>

To query one or more partitions sequentially:

<pre>
usage: kube_cis_polling_simulator.py [-h] --bigip BIGIP
                                     [--bigip_port BIGIP_PORT] --username
                                     USERNAME --password PASSWORD --partitions
                                     PARTITIONS [PARTITIONS ...]

optional arguments:
  -h, --help            show this help message and exit
  --bigip BIGIP         management IP for reaching the BIG-IP REST interface
  --bigip_port BIGIP_PORT
                        port for reaching the BIG-IP REST interface
  --username USERNAME   username for the BIG-IP
  --password PASSWORD   password for the BIG-IP
  --partitions PARTITIONS [PARTITIONS ...]
                        list of partitions separated by spaces
</pre>

To query multiple domains simultaneously, edit and run the bash script:

<pre>
#!/usr/bin/env bash

for run in {1..10}
do
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-1 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-2 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-3 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-4 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-5 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-6 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-7 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-8 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-9 &
    ./kube_cis_polling_simulator.py --bigip bigip13114-dnsohttpstls-6te01x3n.srv.ravcloud.com --username admin --password admin --partitions partition-10 &
sleep 30
done
</pre>