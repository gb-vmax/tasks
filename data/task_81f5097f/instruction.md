A Kubernetes cluster operator needs to validate the structure of a manifest file against a given JSON schema and extract some configuration details from it. You are provided with a deployment manifest in JSON format at /home/user/manifests/nginx-deployment.json and a corresponding JSON schema at /home/user/schemas/deployment-schema.json.

1. Validate that /home/user/manifests/nginx-deployment.json conforms to the schema defined in /home/user/schemas/deployment-schema.json. If the manifest does not conform, record the error messages.
2. If the manifest is valid, extract the following information from the manifest using jq and create a summary file at /home/user/output/manifest_summary.txt in exactly the following format:
    - Name of the deployment (from .metadata.name)
    - Number of replicas (from .spec.replicas)
    - Image name for the first container (from .spec.template.spec.containers[0].image)
    
   The summary file must have three lines, one for each item above, in this format (each item on its own line, without extra spaces):
   
   Name: &lt;deployment-name&gt;
   Replicas: &lt;number-of-replicas&gt;
   Image: &lt;image-name&gt;

3. If schema validation fails, do not create the summary file. Instead, record the validation errors in the file /home/user/output/validation_errors.txt, with each error on its own line, no extra formatting.

Make sure the /home/user/output directory exists and is writeable by the current user before you write to it.
