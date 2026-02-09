# Bug Report

### Describe the bug

Plugin installation is failing because certain npm/yarn deprecation warnings are being incorrectly classified as errors. After a recent update, legitimate deprecation warnings that don't match the exact expected format are causing the installation process to abort.

### Reproduction

Try installing a plugin that has dependencies with deprecation warnings. For example:

```
warning package-name@1.0.0: This package is deprecated. Please update to the latest version.
```

Or:

```
warning some-dep@2.0.0: This package is no longer supported. Please migrate to the new version.
```

The installation fails even though these are just warnings and the plugin should still be installable.

### Expected behavior

Deprecation warnings should be recognized and not block plugin installation. The installer should be able to handle various formats of deprecation messages from npm/yarn, not just one specific format.

### Additional context

This seems to affect plugins with dependencies that have deprecation warnings in different formats than the standard "no longer maintained" message. The installation process is too strict and doesn't account for the variety of ways package managers communicate deprecation information.

---
Repository: /testbed
