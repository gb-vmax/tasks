# Bug Report

### Describe the bug

Plugin installation is failing because legitimate npm/yarn error messages are being incorrectly classified as deprecation warnings. When trying to install a plugin that has actual errors (like missing dependencies or version conflicts), the installation process treats these errors as harmless deprecation warnings and continues instead of failing properly.

### Reproduction

Try installing a plugin that has a real error, for example:

```bash
# Install a plugin with a missing peer dependency
# or a plugin that references a non-existent package version
```

The installation should fail with an error, but instead it succeeds and the plugin doesn't work correctly. The error messages are being filtered out as if they were just deprecation warnings.

### Expected behavior

Real errors during plugin installation should cause the installation to fail, not be silently ignored. Only actual deprecation warnings (like "package X is deprecated, please use Y instead") should be filtered out.

The current behavior is too permissive - it's catching error messages that contain words like "warning" or "deprecated" even when they're part of critical error messages.

### Additional context

This seems to have started happening recently. Previously, plugin installations would properly fail when there were actual problems, but now they're going through even when there are serious issues.

---
Repository: /testbed
