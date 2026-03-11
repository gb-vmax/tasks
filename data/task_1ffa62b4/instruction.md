I'm an edge computing engineer getting ready to deploy firmware configurations to a fleet of IoT sensor devices. I have a master INI configuration file at `/home/user/edge/device_master.ini` that contains settings for multiple components. Before pushing the config to the devices, I need to extract a deployment summary into a flat key=value file that our deployment tool can consume.

Please do the following:

**Step 1:** From the INI file at `/home/user/edge/device_master.ini`, extract specific values from specific sections and write a deployment summary to `/home/user/edge/deploy_summary.conf`.

The INI file has sections including `[device]`, `[network]`, `[sensors]`, and `[thresholds]`. I need you to pull out the following keys and write them to the summary file in this **exact order and format** (no spaces around the `=`, one entry per line):

```
DEVICE_ID=<value of "id" from [device]>
FIRMWARE=<value of "firmware_version" from [device]>
MQTT_HOST=<value of "broker_host" from [network]>
MQTT_PORT=<value of "broker_port" from [network]>
POLL_INTERVAL=<value of "poll_interval_sec" from [sensors]>
TEMP_MAX=<value of "temp_max_celsius" from [thresholds]>
BATTERY_MIN=<value of "battery_min_pct" from [thresholds]>
```

**Step 2:** Append a final line to `/home/user/edge/deploy_summary.conf` that contains a count of how many total keys are defined across the entire INI file (counting every `key = value` line across all sections, ignoring blank lines, comments starting with `;` or `#`, and section headers). The line must be in this exact format:

```
TOTAL_KEYS=<integer count>
```

The finished `/home/user/edge/deploy_summary.conf` must contain exactly 8 lines, nothing more, nothing less. No trailing blank line. Each line must follow the `KEY=value` format exactly as shown above.
