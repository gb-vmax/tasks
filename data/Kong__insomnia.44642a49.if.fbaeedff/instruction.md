# Bug Report

### Describe the bug

Environment variable keys that should be rejected as invalid are now being accepted, and valid keys are being incorrectly flagged as invalid. The validation logic for environment variable key names appears to be inverted.

### Reproduction

When trying to create environment variables:

1. Create an environment variable with a key starting with `$` (e.g., `$myvar`)
   - Expected: Should show error `"$myvar" cannot begin with '$' or contain a '.'`
   - Actual: Key is accepted without error

2. Create an environment variable with a key containing `.` (e.g., `my.var`)
   - Expected: Should show error `"my.var" cannot begin with '$' or contain a '.'`
   - Actual: Key is accepted without error

3. Create an environment variable with a valid key (e.g., `myvar`)
   - Expected: Key should be accepted
   - Actual: Shows error `"myvar" cannot begin with '$' or contain a '.'`

### Expected behavior

Keys starting with `$` or containing `.` should be rejected with an error message, while normal alphanumeric keys should be accepted.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
