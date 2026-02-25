You are a cloud architect migrating legacy server configurations to a new deployment standard. You are provided with a CSV file at /home/user/legacy_services/services.csv containing legacy service records. Each row has the following columns:

service_id, service_name, port, owner, legacy_ip, state

Your goal is to automate the transformation of this data into the format required for import into your new cloud management system, which accepts JSON records—one per line—in a JSON Lines (.jsonl) file, with specific field renaming and filtering requirements. Follow these steps:

1. Read the CSV file located at /home/user/legacy_services/services.csv.
2. For each row where the state is "active", transform it into a JSON object with the following fields:
   - id (takes value from service_id)
   - name (from service_name)
   - endpoint (format: "tcp://<legacy_ip>:<port>")
   - admin (from owner)
3. The resulting JSON objects must each be written as a single line in a new JSON Lines file located at /home/user/legacy_services/active_services.jsonl. Each line must be a valid JSON object as described.
4. After completing the transformation, output a summary log file at /home/user/legacy_services/transform.log. This log must have two lines, formatted as follows:
   Line 1: "Total services found: <count of all services in CSV>"
   Line 2: "Total active services exported: <count of JSON objects in output file>"
   
Be certain that every entry in the output file is correctly transformed and that the log file reflects the true counts. The test will check the contents of both /home/user/legacy_services/active_services.jsonl and /home/user/legacy_services/transform.log for exact correctness.
