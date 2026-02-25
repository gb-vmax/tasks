#!/bin/bash
set -e
cd /home/user

echo "deployment,replicas,container_image" > /home/user/k8s_manifests/deployment_summary.csv && yq -r '.metadata.name + "," + (.spec.replicas|tostring) + "," + .spec.template.spec.containers[0].image' /home/user/k8s_manifests/frontend.yaml >> /home/user/k8s_manifests/deployment_summary.csv && yq -r '.metadata.name + "," + (.spec.replicas|tostring) + "," + .spec.template.spec.containers[0].image' /home/user/k8s_manifests/backend.yaml >> /home/user/k8s_manifests/deployment_summary.csv && yq -r '.metadata.name + "," + (.spec.replicas|tostring) + "," + .spec.template.spec.containers[0].image' /home/user/k8s_manifests/database.yaml >> /home/user/k8s_manifests/deployment_summary.csv
echo "deployment,replicas,container_image" > /home/user/k8s_manifests/deployment_summary.csv && (for f in frontend.yaml backend.yaml database.yaml; do name=$(grep -m1 'name:' /home/user/k8s_manifests/$f | awk '{print $2}'); replicas=$(grep -m1 'replicas:' /home/user/k8s_manifests/$f | awk '{print $2}'); image=$(grep -m1 'image:' /home/user/k8s_manifests/$f | awk '{print $2}'); echo "$name,$replicas,$image"; done) >> /home/user/k8s_manifests/deployment_summary.csv
cat /home/user/k8s_manifests/deployment_summary.csv
