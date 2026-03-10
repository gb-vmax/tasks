I'm an edge computing engineer and I need help processing configuration files for a batch of IoT sensor devices before deploying firmware updates. I have several INI-style config files in `/home/user/iot/configs/` — one per device — and I need to extract, validate, and consolidate them into a single deployment manifest.

Here's the full workflow I need done:

**Step 1: Parse and filter eligible devices**

Each config file is named `device_<ID>.ini` (e.g., `device_A1.ini`). Each file has the following sections and keys (among others):

- `[device]` section: `id`, `model`, `firmware_version`, `enabled`
- `[network]` section: `protocol`, `ip_address`, `port`
- `[sensor]` section: `type`, `sample_rate_hz`, `calibration_offset`
- `[power]` section: `battery_pct`, `sleep_mode`

A device is **eligible for deployment** if ALL of the following are true:
1. `[device] enabled` is `true`
2. `[device] firmware_version` is strictly less than `2.0` (treat as a float comparison)
3. `[power] battery_pct` is greater than or equal to `20` (treat as integer)

Devices that fail any of these checks are **ineligible**.

**Step 2: Generate the deployment manifest**

Write the results to `/home/user/iot/deployment_manifest.txt` with exactly this format:

```
=== IoT Deployment Manifest ===
Generated for: edge-cluster-07
Total devices scanned: <N>
Eligible for deployment: <N>
Ineligible (skipped): <N>

--- ELIGIBLE DEVICES ---
[<device_id>]
  Model:              <model>
  Current Firmware:   <firmware_version>
  Network:            <protocol>://<ip_address>:<port>
  Sensor Type:        <type>
  Sample Rate:        <sample_rate_hz> Hz
  Calibration Offset: <calibration_offset>
  Battery:            <battery_pct>%
  Sleep Mode:         <sleep_mode>

(one blank line between device blocks, no trailing blank line after the last device)

--- INELIGIBLE DEVICES ---
[<device_id>] SKIP: <reason>

(listed in order, one per line)
```

The eligible devices must be listed in **ascending alphabetical order by device ID**. The ineligible devices must also be listed in **ascending alphabetical order by device ID**.

For ineligible devices, the `<reason>` field must be exactly one of:
- `disabled` — if `enabled` is not `true` (check this first)
- `firmware current (X.X)` — if firmware_version >= 2.0 (where X.X is the actual firmware_version value from the file, e.g. `firmware current (2.1)`)
- `low battery (N%)` — if battery_pct < 20 (where N is the actual battery_pct value, e.g. `low battery (15%)`)

If a device is ineligible for multiple reasons, report only the **first failing reason** in the priority order listed above (disabled → firmware → battery).

The manifest header line `Generated for: edge-cluster-07` is a fixed string.

**Step 3: Compute and append a summary of sensor statistics for eligible devices only**

Append the following block at the end of the manifest (after the ineligible section), with no blank line separating it from the ineligible section's last line:

```

--- SENSOR STATISTICS (eligible devices) ---
Sensor types present: <comma-separated sorted list of unique sensor types>
Average sample rate: <value> Hz
Highest calibration offset: <value>
Lowest calibration offset: <value>
```

- Average sample rate should be rounded to 2 decimal places (e.g., `12.50 Hz`)
- Calibration offsets are signed floats; report the raw value as it appears (e.g., `-0.5` or `1.2`)
- Sensor types should be sorted alphabetically and comma-separated with a single space after each comma

The final file must end with a newline character after the last statistics line.
