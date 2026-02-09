# Bug Report

### Describe the bug

Plugin installation is failing when encountering certain deprecation warnings from yarn. The installation process seems to be incorrectly treating valid deprecation warnings as errors and blocking the plugin from being installed.

### Reproduction

When trying to install a plugin that has deprecated dependencies, the installation fails even though these are just warnings and shouldn't prevent the plugin from working.

For example, when installing a plugin with dependencies that show deprecation messages like:
- "package X is no longer maintained"
- "package Y is not recommended for usage"  
- "please upgrade your dependencies"

The plugin installation gets blocked instead of proceeding with just a warning.

### Expected behavior

Deprecation warnings from yarn should not prevent plugin installation. The plugin should install successfully and the warnings should be logged, but not treated as blocking errors. Only actual installation failures should prevent the plugin from being installed.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
