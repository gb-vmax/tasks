#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/output && touch /home/user/output/test_write_perm && rm /home/user/output/test_write_perm
ajv validate -s /home/user/schemas/deployment-schema.json -d /home/user/manifests/nginx-deployment.json --errors=text 2>&1
jsonschema -i /home/user/manifests/nginx-deployment.json /home/user/schemas/deployment-schema.json 2>&1
python3 -m jsonschema -i /home/user/manifests/nginx-deployment.json /home/user/schemas/deployment-schema.json 2>&1
which pip3
pip3 install --user jsonschema
python3 -m jsonschema -i /home/user/manifests/nginx-deployment.json /home/user/schemas/deployment-schema.json 2>&1
jq -r '"Name: \(.metadata.name)\nReplicas: \(.spec.replicas)\nImage: \(.spec.template.spec.containers[0].image)"' /home/user/manifests/nginx-deployment.json > /home/user/output/manifest_summary.txt
cat /home/user/output/manifest_summary.txt
