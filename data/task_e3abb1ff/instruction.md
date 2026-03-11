I'm an edge computing engineer managing a fleet of IoT sensors. I have a device registry file at `/home/user/iot/devices.csv` that was exported from our management platform. It contains more columns than I need for my deployment script, and the columns are in the wrong order.

The file currently has these columns (comma-separated):
`device_id,location,firmware_version,ip_address,status,last_seen`

For the deployment tool I'm running, I need a new file at `/home/user/iot/deploy_targets.csv` that contains **only** the `ip_address`, `device_id`, and `firmware_version` columns — **in that exact order** — with no header line and using a colon (`:`) as the delimiter instead of a comma.

For example, if the input file has a row like:
```
sensor-004,warehouse-b,2.1.0,10.0.0.44,active,2024-11-01
```

Then the corresponding output row should be:
```
10.0.0.44:sensor-004:2.1.0
```

Please create the output file `/home/user/iot/deploy_targets.csv` with the correctly ordered and formatted data. The file should contain only the data rows (no header), one device per line, in the same order as the input file.
