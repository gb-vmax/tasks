You are an infrastructure engineer and need to automate part of the cloud provisioning workflow. In your home directory (/home/user), you have a file named /home/user/server_inventory.csv with the following columns: hostname, ip_address, os_type, provisioned. The file contains a list of planned servers, but you must automate the next steps as follows:

1. Read /home/user/server_inventory.csv and identify all servers where the column 'provisioned' is 'no'.
2. For each unprovisioned server, generate a provisioning JSON request and write it into a separate file named /home/user/provision_requests.json. The output must be a single JSON array, where each element is a JSON object corresponding to a server with the following fields: "hostname", "ip_address", "os_type".
   - The output file must have an array with only unprovisioned servers, each as described above. The file must be pretty-printed (indented with 4 spaces).
   - For example, the structure must look like:
     [
         {
             "hostname": "srv1",
             "ip_address": "10.0.0.1",
             "os_type": "ubuntu"
         },
         ... 
      ]
3. Update /home/user/server_inventory.csv such that all servers which were marked as provisioned 'no', are now updated to 'yes'.
   - The resulting CSV must have the same columns, and the only changes should be that 'provisioned' is set to 'yes' where it was 'no'.
4. Create a log file at /home/user/provisioning_audit.log. For every changed row, write a log entry in this format:
   [YYYY-MM-DD HH:MM:SS] Changed server <hostname> provisioning status from 'no' to 'yes'
   - Use the current date and time for each log entry.
   - Each log entry must be on its own line.

Be sure the output files exactly match the format described, as automated checks will verify the structure and correctness.
