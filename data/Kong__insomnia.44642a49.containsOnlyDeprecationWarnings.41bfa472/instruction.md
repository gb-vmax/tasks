# Bug Report

### Describe the bug

Plugin installation is failing when npm outputs non-deprecation warnings or errors. It looks like the validation logic for checking if stderr contains only deprecation warnings is not working correctly. 

I'm seeing cases where legitimate errors during plugin installation are being ignored, and the installation appears to succeed even though it should have failed.

### Reproduction

Try installing a plugin that produces npm warnings or errors (not just deprecation warnings). For example:

1. Install a plugin with a peer dependency warning
2. Or install a plugin where npm outputs an error message along with deprecation warnings
3. The installation completes successfully even though there were actual errors

### Expected behavior

Plugin installation should fail if there are any non-deprecation errors or warnings in the npm stderr output. Only pure deprecation warnings should be allowed to pass through as successful installations.

The current behavior seems to allow installations to succeed even when there are real problems that should cause the installation to fail.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
