# Bug Report

### Describe the bug

Plugin installation is failing when npm outputs peer dependency or security warnings. The installation process treats these warnings as errors and aborts, even though the plugin itself may have installed successfully.

### Reproduction

Try installing a plugin that has peer dependency warnings or security vulnerability warnings in its dependency tree. For example:

```bash
# Install a plugin that has peer dependency warnings
# The installation will fail even though the plugin works fine
```

The issue occurs because the plugin installer only recognizes deprecation warnings as "safe" warnings that can be ignored. Any other warning types (peer dependency mismatches, security advisories) cause the installation to fail.

### Expected behavior

Plugin installation should succeed when npm outputs peer dependency warnings or security warnings, similar to how it handles deprecation warnings. These warnings should be logged to the console but shouldn't prevent the plugin from being installed.

### System Info

- Insomnia version: latest
- OS: Any

---
Repository: /testbed
