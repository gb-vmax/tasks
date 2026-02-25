#!/bin/bash
set -e
cd /home/user

grep -i '^kind:' /home/user/k8s-manifests/deployment.yaml /home/user/k8s-manifests/service.yaml /home/user/k8s-manifests/configmap.yaml | sed -n 's/^.*kind:[[:space:]]*\(.*\)$/\1/pI' | tr '[:lower:]' '[:upper:]' | sort | uniq -c | awk '{print $2" "$1}' | sort > /home/user/k8s-manifests/kind_frequency.log
cat /home/user/k8s-manifests/kind_frequency.log
