# Bug Report

### Describe the bug

Plugin installation is failing to properly detect deprecated dependency warnings from Yarn. The system appears to be incorrectly identifying certain deprecation messages, which may cause plugins with deprecated dependencies to not install properly or show incorrect warnings.

### Reproduction

When installing a plugin that has deprecated dependencies, the deprecation warning detection doesn't work as expected. The issue occurs specifically when Yarn outputs deprecation warnings with the message "not recommended for usage" in the warning text.

Example scenario:
1. Install a plugin with deprecated dependencies
2. Yarn outputs a deprecation warning containing "no longer maintained" and "not recommended for usage"
3. The warning is not properly recognized as a deprecation warning

### Expected behavior

The system should correctly identify deprecation warnings from Yarn regardless of the exact wording used in the warning message. Plugins with deprecated dependencies should still be installable with appropriate warnings shown to the user.

### Additional context

This seems to be related to how the deprecation warning messages are parsed. The detection logic may be too strict or looking for specific text that doesn't always match what Yarn actually outputs.

---
Repository: /testbed
