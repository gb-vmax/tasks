#!/bin/bash
set -e
cd /home/user

ls /home/user/etl/incoming/
cd /home/user/etl/incoming/ && sha256sum customers.csv orders.csv products.csv | sort -k2 > /home/user/etl/checksums.sha256
cat /home/user/etl/checksums.sha256
cd /home/user/etl/incoming/ && sha256sum --check /home/user/etl/checksums.sha256
