# Bug Report

### Describe the bug

Plugin installation is failing with deprecation warnings from dependencies. The system is incorrectly identifying deprecation warnings and blocking plugin installation when it should allow it to proceed.

### Reproduction

Try installing a plugin that has dependencies with deprecation warnings from yarn. The installation gets blocked even though these are just warnings and the plugin should still be installable.

Example scenario:
1. Install a plugin with a deprecated dependency
2. Yarn outputs deprecation warning message
3. Installation fails unexpectedly

The warning message typically contains text like "no longer maintained" or "not recommended for usage" but the plugin installation should still succeed since these are warnings, not errors.

### Expected behavior

Deprecation warnings from yarn should be properly detected and the plugin installation should proceed successfully. The system should only block installation on actual errors, not on deprecation warnings.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
