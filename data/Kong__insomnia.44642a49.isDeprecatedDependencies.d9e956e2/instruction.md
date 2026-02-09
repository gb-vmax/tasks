# Bug Report

### Describe the bug

After a recent update, the plugin installation process is incorrectly treating certain npm/yarn error messages as deprecation warnings. This causes actual installation errors to be silently ignored, making it appear as though plugins installed successfully when they actually failed.

### Reproduction

When attempting to install a plugin that has a legitimate installation error (not just a deprecation warning), the error is not properly surfaced to the user. The installation appears to succeed but the plugin is not functional.

For example, installing a plugin that triggers an error message like:
```
Error: Cannot find module 'some-required-dependency'
```

This gets incorrectly classified as a deprecation warning and the installation is treated as successful.

### Expected behavior

Only actual deprecation warnings should be treated as non-critical. Real errors during plugin installation should be reported to the user and the installation should be marked as failed.

The function should distinguish between:
- Actual deprecation warnings (which can be ignored)
- Critical installation errors (which should fail the installation)

### Additional context

This seems to be related to the logic that determines whether stderr output contains only deprecation warnings. The detection appears to be too broad and is catching error messages that contain keywords like "warning" or "deprecated" even when they're part of actual error messages.

---
Repository: /testbed
