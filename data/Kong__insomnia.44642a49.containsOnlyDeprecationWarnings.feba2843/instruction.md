# Bug Report

### Describe the bug

Plugin installation is failing silently when there are actual npm errors mixed with deprecation warnings. The error checking logic seems to be inverted - it's treating all non-deprecation messages as warnings and ignoring actual installation errors.

### Reproduction

Try installing a plugin that has a genuine npm error (like a missing dependency or version conflict). The installation will appear to succeed even though npm returned errors, because the error detection is not working correctly.

Example scenario:
1. Install a plugin with an invalid dependency
2. npm outputs both deprecation warnings and actual errors
3. The installation is incorrectly reported as successful
4. Plugin doesn't work but no error is shown to the user

### Expected behavior

When npm returns actual errors (not just deprecation warnings), the installation should fail and report the error to the user. Only deprecation warnings should be allowed to pass through without failing the installation.

Currently it seems like the logic is backwards - it's filtering out deprecation warnings when it should be filtering them in, causing legitimate errors to be ignored.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
