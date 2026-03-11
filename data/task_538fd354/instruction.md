Hey, I'm a deployment engineer and I need your help processing our deployment manifest before rolling out updates. We have a JSON file at `/home/user/deployments/manifest.json` that contains a list of service deployments. I need to extract only the services that are ready for deployment and write a summary file.

Here's what I need you to do:

**Step 1:** Use `jq` to filter the manifest and extract only the services where `"status"` is `"ready"` AND `"environment"` is `"production"`. From those filtered entries, output a new JSON array containing objects with only three fields: `"service"`, `"version"`, and `"replicas"`. Write the result to `/home/user/deployments/production_ready.json`.

The output file must be a valid JSON array, pretty-printed with 2-space indentation (jq's default). The objects in the array must appear in the same order as they appear in the original manifest. Each object must contain exactly and only the fields `service`, `version`, and `replicas` — no other fields.

**Step 2:** Using `jq` again (or any standard tool), count the total number of replicas across all services in `/home/user/deployments/production_ready.json` and write just the integer number (followed by a newline) to `/home/user/deployments/replica_count.txt`.

The file `/home/user/deployments/replica_count.txt` must contain exactly one line: the total replica count as a plain integer with no extra text, spaces, or formatting.

For example, if the production-ready services have 3, 5, and 2 replicas respectively, the file should contain:
```
10
```

Please process the manifest and produce both output files.
