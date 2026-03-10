I'm migrating our legacy services to a new cloud infrastructure and I need to document the current service configuration before decommissioning the old instances. We have an old Python service inventory script sitting at `/home/user/legacy/service_inventory.py` that was written years ago. I need you to run it and capture its output into a migration artifact.

Here's the situation: the script prints service configuration data to stdout when executed. I need you to:

1. Run the legacy script at `/home/user/legacy/service_inventory.py` using Python 3 and redirect its full stdout output into a file at `/home/user/migration/inventory_raw.txt`. Create the `/home/user/migration/` directory first if it doesn't exist.

2. The script outputs lines in this format:
   ```
   SERVICE=<name> HOST=<hostname> PORT=<port> STATUS=<status>
   ```
   From `inventory_raw.txt`, extract only the lines where `STATUS=active` and write them to `/home/user/migration/active_services.txt`. The file should contain only the matching lines, one per line, in the same order they appear in the raw output.

3. Count the number of active services extracted and append a summary line to the end of `/home/user/migration/active_services.txt`. The summary line must be exactly:
   ```
   TOTAL_ACTIVE=<N>
   ```
   where `<N>` is the integer count of active service lines (not counting the summary line itself).

The final `/home/user/migration/active_services.txt` should contain only the `STATUS=active` lines followed by the single `TOTAL_ACTIVE=<N>` line at the very end. No blank lines, no extra whitespace. The automated test will check the exact contents of both `inventory_raw.txt` and `active_services.txt`.
