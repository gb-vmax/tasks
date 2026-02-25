You are a Kubernetes operator who needs to summarize information from your deployment manifests. In the directory <code>/home/user/k8s_manifests</code>, there are three Kubernetes Deployment manifest files in YAML format: <code>frontend.yaml</code>, <code>backend.yaml</code>, and <code>database.yaml</code>. Each file contains a <code>Deployment</code> resource including metadata (with at least a <code>name</code> field) and a specification (<code>spec</code>) with a <code>replicas</code> field and a container defined under <code>spec.template.spec.containers</code> that contains a <code>name</code> and an <code>image</code> field.

Your task is:

1. Parse all three YAML files and extract the following fields for each deployment:
   - <b>Deployment Name:</b> from <code>metadata.name</code>
   - <b>Replicas:</b> from <code>spec.replicas</code>
   - <b>Container Image:</b> the <code>image</code> property of the first container listed in <code>spec.template.spec.containers</code>

2. Output this information as a single CSV file located at <code>/home/user/k8s_manifests/deployment_summary.csv</code> with the following format (including the header row):

<pre>
deployment,replicas,container_image
frontend,3,nginx:1.19
backend,2,python:3.9
database,1,mongo:4.4
</pre>

Make sure the columns are named exactly as above, and that each deployment's data appears in the order: frontend, backend, database. Include the appropriate newline characters such that each record is on its own line. Ensure the CSV file strictly matches the format shown above.
