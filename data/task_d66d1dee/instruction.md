I'm a DevSecOps engineer and I need help enforcing a security benchmark policy against a scanned system configuration. I have two files already set up on my machine:

1. `/home/user/policy/benchmark.json` — a JSON file defining the required security thresholds for several controls.
2. `/home/user/policy/scan_results.json` — a JSON file containing the actual measured values from the target system.

I need you to compare the scan results against the benchmark policy and write a compliance report to `/home/user/policy/compliance_report.txt`.

Here's exactly how the comparison works:

- Each control in `benchmark.json` has a `control_id`, a `description`, a `threshold` (a numeric limit), and a `operator` field which is either `"lte"` (the scanned value must be **less than or equal to** the threshold to pass) or `"gte"` (the scanned value must be **greater than or equal to** the threshold to pass).
- Each entry in `scan_results.json` has a `control_id` and a `value` (the measured numeric value from the system).
- A control **PASSES** if its operator condition is satisfied (e.g., `operator: "lte"` and `value <= threshold`).
- A control **FAILS** if the condition is not satisfied.

The output file `/home/user/policy/compliance_report.txt` must have this **exact** format:

```
=== SECURITY BENCHMARK COMPLIANCE REPORT ===

CONTROL RESULTS:
  [PASS] <control_id>: <description> (expected <operator> <threshold>, got <value>)
  [FAIL] <control_id>: <description> (expected <operator> <threshold>, got <value>)
  ...

SUMMARY:
Total controls: <N>
Passed: <N>
Failed: <N>
Compliance: <percentage>%

OVERALL STATUS: <COMPLIANT or NON-COMPLIANT>
```

Formatting rules:
- Controls must be listed in the order they appear in `benchmark.json`.
- The `<operator>` in the output must be written exactly as it appears in the JSON (`lte` or `gte`).
- `<threshold>` and `<value>` must be printed as integers (no decimal point).
- `<percentage>` is `(Passed / Total) * 100`, rounded to the nearest whole number, also as an integer (no decimal point).
- `OVERALL STATUS` is `COMPLIANT` if all controls pass, otherwise `NON-COMPLIANT`.
- There must be exactly two spaces of indentation before each `[PASS]` or `[FAIL]` line.

Please produce the report at `/home/user/policy/compliance_report.txt`.
