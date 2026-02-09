# Bug Report

### Describe the bug

After updating to the latest version, plugin installation is failing with deprecation warnings that used to work fine before. The installation process now seems to be treating deprecation warnings differently, and plugins that have deprecated dependencies are being blocked from installation.

### Reproduction

1. Try to install a plugin that has deprecated dependencies (e.g., a plugin using an older version of a popular npm package)
2. The installation fails even though these are just deprecation warnings, not actual errors
3. Previously these warnings were logged but the plugin would still install successfully

Example plugin scenario:
- Plugin depends on a package with deprecated dependencies
- npm outputs deprecation warnings during installation
- Installation now fails instead of completing with warnings

### Expected behavior

Deprecation warnings should be logged to the console for visibility, but they shouldn't prevent plugin installation from completing successfully. The plugin should install and work normally, with the warnings displayed so developers are aware of the deprecated dependencies.

### Additional context

This appears to have started happening recently. The behavior changed from allowing installations with deprecation warnings to blocking them entirely. This breaks compatibility with many existing plugins that haven't updated their dependencies yet but are otherwise functional.

---
Repository: /testbed
