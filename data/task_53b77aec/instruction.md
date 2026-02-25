A Kubernetes operator provided you with a JSON manifest describing a list of Kubernetes pods, saved at <code>/home/user/k8s_pods.json</code>. Your task is to:

1. Parse <code>/home/user/k8s_pods.json</code> and extract all pod names whose status is "Running".
2. Output the names of these running pods in a CSV file located at <code>/home/user/running_pods.csv</code>, where the top row must be the header "pod_name", and each subsequent row contains a single pod name.
3. Be careful to match the expected CSV file format exactly: it must use LF line endings, no additional whitespace, and the file must only contain pod names in the "Running" state as found in the input JSON.

For verification, provide only the specified CSV output, ensuring the format matches exactly as described above.
