#!/bin/bash
# Ground truth reference (not an executable solution):
#
# Initial files present before the task starts:
# 
# /home/user/old-operator/deployment.yaml:
# ```
# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: old-app-deployment
# spec:
#   replicas: 1
#   selector:
#     matchLabels:
#       app: old-app
#   template:
#     metadata:
#       labels:
#         app: old-app
#     spec:
#       containers:
#       - name: old-app-container
#         image: old-app-image:v1.2.3
#         ports:
#         - containerPort: 80
# ```
# 
# /home/user/old-operator/service.yaml:
# ```
# apiVersion: v1
# kind: Service
# metadata:
#   name: old-app-service
# spec:
#   selector:
#     app: old-app
#   ports:
#     - protocol: TCP
#       port: 80
#       targetPort: 80
#   type: ClusterIP
# ```
# 
# After correct completion, these files should exist:
# 
# /home/user/old-operator/deployment.yaml:
# ```
# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: old-app-deployment
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: old-app
#   template:
#     metadata:
#       labels:
#         app: old-app
#     spec:
#       containers:
#       - name: old-app-container
#         image: old-app-image:v1.2.3
#         ports:
#         - containerPort: 80
# ```
# 
# /home/user/old-operator/service.yaml: (unchanged)
# ```
# apiVersion: v1
# kind: Service
# metadata:
#   name: old-app-service
# spec:
#   selector:
#     app: old-app
#   ports:
#     - protocol: TCP
#       port: 80
#       targetPort: 80
#   type: ClusterIP
# ```
# 
# /home/user/old-operator/validation_report.txt:
# ```
# Validation Report for Kubernetes Manifests
# 
# deployment.yaml: OK
# service.yaml: OK
# ```
# 
# /home/user/old-operator/apply_dryrun.log:
# ```
# deployment.apps/old-app-deployment configured (dry run)
# service/old-app-service configured (dry run)
# ```

echo 'No automated solution provided.'
