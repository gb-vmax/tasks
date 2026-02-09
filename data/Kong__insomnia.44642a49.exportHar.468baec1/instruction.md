# Bug Report

### Describe the bug

After a recent update, HAR exports are generating incorrect timing values. The `send`, `wait`, and `receive` timings are now being calculated and populated with estimated values instead of using the actual timing data. This causes issues when importing HAR files into analysis tools that rely on accurate timing information.

### Reproduction

1. Create a request in Insomnia
2. Send the request and get a response
3. Export the request as HAR format
4. Open the exported HAR file and inspect the `timings` object

Expected timings structure:
```json
{
  "blocked": -1,
  "dns": -1,
  "connect": -1,
  "send": 0,
  "wait": <actual_elapsed_time>,
  "receive": 0,
  "ssl": -1
}
```

Actual timings structure (incorrect):
```json
{
  "blocked": -1,
  "dns": -1,
  "connect": -1,
  "send": <some_estimated_value>,
  "wait": <calculated_value>,
  "receive": <some_estimated_value>,
  "ssl": -1
}
```

The timing values are now being split up and estimated based on content size and total elapsed time, which doesn't reflect the actual network timing breakdown. This is particularly problematic because Insomnia doesn't have access to the granular timing data, so these "enhanced" timings are just guesses.

### Expected behavior

HAR exports should maintain the previous behavior where only the `wait` field contains the actual elapsed time and other timing fields that aren't available should remain at 0 or -1. This accurately represents what timing data is actually available rather than generating misleading estimated values.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
