#!/bin/bash
set -e
cd /home/user

awk -F, 'NR==1{split($0,headers); next} {printf "%s{\"%s\":\"%s\",\"%s\":\"%s\",\"%s\":\"%s\",\"%s\":\"%s\"}", (NR==2?"[":","), headers[1],$1,headers[2],$2,headers[3],$3,headers[4],$4} END{print "]"}' /home/user/k8s-manifests/deployments.csv > /home/user/k8s-manifests/deployments.json
jq 'map(if .name=="backend" and .namespace=="prod" then .replicas="5" else . end)' /home/user/k8s-manifests/deployments.json > /home/user/k8s-manifests/deployments.json.tmp && mv /home/user/k8s-manifests/deployments.json.tmp /home/user/k8s-manifests/deployments.json
sed -Ez 's/(\{[^}]*"name":"backend"[^}]*"namespace":"prod"[^}]*"replicas":")([0-9]+)(")/\15\3/' /home/user/k8s-manifests/deployments.json > /home/user/k8s-manifests/deployments.json.tmp && mv /home/user/k8s-manifests/deployments.json.tmp /home/user/k8s-manifests/deployments.json
echo 'Updated backend in prod: replicas set to 5' > /home/user/k8s-manifests/update.log
