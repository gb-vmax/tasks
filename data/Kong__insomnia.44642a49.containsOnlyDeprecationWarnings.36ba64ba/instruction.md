# Bug Report

### Describe the bug

I'm experiencing an issue with plugin installation where npm warnings/errors aren't being handled correctly. It seems like the validation logic for determining whether stderr output contains only deprecation warnings is broken.

### Reproduction

When installing a plugin that produces both deprecation warnings AND actual errors, the installation appears to succeed when it should fail. 

For example, if npm outputs:
- 2 deprecation warnings
- 1 actual error message

The system incorrectly treats this as "only deprecation warnings" and continues with the installation instead of failing.

### Expected behavior

The installation should fail if there are any non-deprecation errors in the stderr output. Only when stderr contains exclusively deprecation warnings (or is empty) should the installation proceed.

Currently it seems like the logic for counting warnings vs errors is off - installations are succeeding even when there are real errors mixed in with the deprecation warnings.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
