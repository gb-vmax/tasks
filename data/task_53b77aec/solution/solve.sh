#!/bin/bash
set -e
cd /home/user

jq -r '.items[] | select(.status.phase=="Running") | .metadata.name' /home/user/k8s_pods.json | awk 'BEGIN{print "pod_name"} {print}' > /home/user/running_pods.csv
sudo apt-get update && sudo apt-get install -y jq
apt-get update && apt-get install -y jq
jq -r '.items[] | select(.status.phase=="Running") | .metadata.name' /home/user/k8s_pods.json | awk 'BEGIN{print "pod_name"} {print}' > /home/user/running_pods.csv
head -20 /home/user/k8s_pods.json
jq -r '.pods[] | select(.status=="Running") | .name' /home/user/k8s_pods.json | awk 'BEGIN{print "pod_name"} {print}' > /home/user/running_pods.csv
cat /home/user/running_pods.csv
