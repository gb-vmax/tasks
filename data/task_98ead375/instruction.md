A DevSecOps policy requires that all containers approved for production deployment must have images that come from the "corporate" registry. A CSV file located at /home/user/containers/inventory.csv contains a list of containers and their image sources. It has the following columns: container_name,image_source. Your task is to:

1. Read the /home/user/containers/inventory.csv file.
2. For each row, check if the "image_source" field starts with "registry.corporate.com/".
3. Create a JSON policy compliance report at /home/user/output/policy_report.json, listing ONLY the containers that fail this check. The JSON report should be an array of objects with these fields: container_name, image_source, and compliance (which must have value "FAIL").
4. The output JSON file must look like this format:
[
  {
    "container_name": "app1",
    "image_source": "docker.io/library/app1:latest",
    "compliance": "FAIL"
  },
  {
    "container_name": "testservice",
    "image_source": "quay.io/example/testservice:1.1",
    "compliance": "FAIL"
  }
]

Note:
- Include only the non-compliant containers in the report.
- The /home/user/containers/inventory.csv file already exists and is readable, and the /home/user/output directory is writable.
- Ensure the final JSON output is valid and matches the exact format above for automated verification.
