Hey, I need help analyzing telemetry logs from our IoT edge deployment. We have sensor devices across three zones — factory floor, warehouse, and outdoor — and I need to generate a frequency analysis report from their event logs. Can you process the log files and produce a unified summary?

The raw log files are in `/home/user/iot_logs/`. There are three files:

- `/home/user/iot_logs/zone_factory.log`
- `/home/user/iot_logs/zone_warehouse.log`
- `/home/user/iot_logs/zone_outdoor.log`

Each line in these files is a single event code string like `ERR_SENSOR_TIMEOUT` or `WARN_LOW_BATTERY`. Lines may repeat, and there may be blank lines (ignore them).

I need you to do three things **independently** for each zone file, then combine the results into a single report:

**Per-zone analysis:**
For each zone file, count the frequency of each unique event code (ignoring blank lines), then identify:
1. The top 3 most frequent event codes and their counts (sorted by count descending; if there's a tie, sort alphabetically ascending by event code).
2. The total number of events (non-blank lines) in that zone file.
3. The total number of distinct event codes in that zone file.

**Cross-zone analysis:**
After processing each zone independently, identify which event code appears (i.e., occurs at least once) in all three zone files. If multiple codes appear in all three zones, list them all alphabetically. If none appear in all three zones, write `NONE`.

Also compute the grand total: sum of all events across all three zone files.

**Write the final report to `/home/user/iot_logs/telemetry_report.txt`** with this exact format (including spacing and punctuation):

```
=== IoT Telemetry Frequency Report ===

[ZONE: factory]
Total events: <N>
Distinct codes: <N>
Top 3:
  1. <EVENT_CODE> (<count>)
  2. <EVENT_CODE> (<count>)
  3. <EVENT_CODE> (<count>)

[ZONE: warehouse]
Total events: <N>
Distinct codes: <N>
Top 3:
  1. <EVENT_CODE> (<count>)
  2. <EVENT_CODE> (<count>)
  3. <EVENT_CODE> (<count>)

[ZONE: outdoor]
Total events: <N>
Distinct codes: <N>
Top 3:
  1. <EVENT_CODE> (<count>)
  2. <EVENT_CODE> (<count>)
  3. <EVENT_CODE> (<count>)

[CROSS-ZONE]
Codes present in all 3 zones: <EVENT_CODE1>,<EVENT_CODE2>,...
Grand total events: <N>
```

A few formatting rules to be precise about:
- Zone names in the headers are lowercase (`factory`, `warehouse`, `outdoor`).
- The "Codes present in all 3 zones" line lists codes separated by commas with NO spaces between them, sorted alphabetically ascending. If none, just write `NONE`.
- The Top 3 list uses 2-space indentation before the number.
- There is a blank line between each zone section and before `[CROSS-ZONE]`.
- There is NO trailing blank line after the last line of the file.

Please process the three zone files in parallel (independently) to compute per-zone stats, then combine everything into the report file.
</think>
