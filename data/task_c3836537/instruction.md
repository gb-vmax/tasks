Hey, I need your help setting up a quick uptime check for a few of our internal services. We have a file at `/home/user/monitoring/hosts.txt` that lists hostnames (one per line). I want you to write a shell script that reads this file and checks whether each host is reachable, then run it to produce a status report.

Here's what I need:

**1. Write the monitoring script**

Create a shell script at `/home/user/monitoring/check_uptime.sh`. The script should:

- Read each line from `/home/user/monitoring/hosts.txt` (ignoring blank lines and lines starting with `#`)
- For each host, attempt to ping it with exactly **2 packets** and a **timeout of 3 seconds** (use `ping -c 2 -W 3`)
- Record whether the host is `UP` or `DOWN` based on whether all packets were received (exit code 0 = UP, non-zero = DOWN)
- Write the results to `/home/user/monitoring/uptime_report.txt` in this exact format:

```
=== Uptime Report ===
Timestamp: <YYYY-MM-DD HH:MM:SS>
Hosts checked: <N>

Status:
  <hostname>: UP
  <hostname>: DOWN
  ...

Summary:
  UP:   <count>
  DOWN: <count>
```

Where:
- `<YYYY-MM-DD HH:MM:SS>` is the time the script was run, formatted with `date '+%Y-%m-%d %H:%M:%S'`
- Hosts are listed in the same order they appear in `hosts.txt`
- The spacing in the Summary section uses exactly 2 spaces of indentation, then the label, then enough spaces so that the counts are aligned — specifically `UP:   <count>` (UP followed by 3 spaces then the count) and `DOWN: <count>` (DOWN followed by 1 space then the count)

Make the script executable.

**2. Run the script**

Execute `/home/user/monitoring/check_uptime.sh` to generate the report at `/home/user/monitoring/uptime_report.txt`.

The hosts file contains a mix of reachable and unreachable hostnames. `localhost` will be UP, and the fake hostnames will be DOWN. Make sure the script handles both cases correctly so the report reflects accurate UP/DOWN status.

The final report file must exist at `/home/user/monitoring/uptime_report.txt` and follow the format above exactly, including the spacing, the `===` header, and all section labels. The automated test will check the structure and the UP/DOWN classification of each host.
