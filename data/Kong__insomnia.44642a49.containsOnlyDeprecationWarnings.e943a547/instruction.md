# Bug Report

### Describe the bug

The plugin installation process is incorrectly reporting success when npm outputs errors alongside deprecation warnings. After a recent change, any stderr output containing at least one deprecation warning is treated as successful, even if there are actual errors present.

### Reproduction

1. Attempt to install a plugin that triggers both deprecation warnings and actual npm errors
2. The installation is marked as successful despite the errors
3. The plugin may not be properly installed but no error is shown to the user

Example scenario:
- Install a plugin with deprecated dependencies that also has a genuine installation error (e.g., network timeout, missing dependency)
- The deprecation warning is detected and the function returns `true` (success)
- The actual error is ignored

### Expected behavior

The installation should only be considered successful if stderr contains **only** deprecation warnings and no other errors. If there are any non-deprecation errors present, the installation should be marked as failed.

Previously, the function would verify that all lines in stderr were deprecation warnings. Now it only checks if there's at least one deprecation warning, which is incorrect.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
