#!/usr/bin/env bash

for run in {1..10}
do
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-1 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-2 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-3 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-4 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-5 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-6 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-7 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-8 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-9 &
    ./kube_cis_polling_simulator.py --bigip 10.1.0.24 --username admin --password admin --partitions partition-10 &
sleep 30
done
