# Bug Report

### Describe the bug

The menu bar visibility toggle is not working correctly. When trying to hide the menu bar, it remains visible, and when trying to show it, it gets hidden instead. The behavior appears to be inverted from what's expected.

### Reproduction

Steps to reproduce:
1. Open the application
2. Try to hide the menu bar through the settings/view menu
3. The menu bar remains visible instead of hiding
4. Try to show the menu bar when it's supposed to be hidden
5. The menu bar gets hidden instead

### Expected behavior

When setting menu bar visibility to `false`, the menu bar should be hidden and auto-hide should be enabled. When setting it to `true`, the menu bar should be visible and auto-hide should be disabled.

Currently experiencing the opposite behavior - the visibility state seems to be inverted.

### System Info
- Insomnia version: latest
- OS: Cross-platform (affects all operating systems)
- Electron-based application

---
Repository: /testbed
