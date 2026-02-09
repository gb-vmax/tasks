# Bug Report

### Describe the bug

Plugin installation is failing with errors being treated as warnings. When npm outputs actual errors during plugin installation, they're being ignored and the installation is reported as successful even though it failed.

### Reproduction

Try installing a plugin that has installation errors (not just deprecation warnings). For example:

1. Attempt to install a plugin with a broken dependency
2. npm outputs errors to stderr
3. The installation completes "successfully" instead of failing

The issue seems to be with how stderr output is being filtered and validated. Empty lines are being kept while actual error messages are being filtered out, causing the validation logic to incorrectly determine that only deprecation warnings are present.

### Expected behavior

- Real installation errors should cause the installation to fail
- Only deprecation warnings should be allowed to pass through
- Empty lines in stderr should be filtered out, not kept

### System Info

- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
