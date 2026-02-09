# Bug Report

### Describe the bug

After a recent update, keyboard shortcuts are not working properly in some cases. When I have custom hotkey bindings configured, certain shortcuts stop responding or behave unexpectedly. It seems like the hotkey registry might be getting corrupted or reset during application startup.

### Reproduction

1. Configure custom keyboard shortcuts in settings
2. Restart the application
3. Try to use the custom shortcuts - some of them don't work anymore
4. Check the settings and notice that some bindings have been changed back to defaults

For example, if I set a custom binding for a specific action and then restart, the binding either disappears or gets replaced with the default one, even though I never explicitly reset it.

### Expected behavior

Custom keyboard shortcuts should persist across application restarts and continue to work as configured. The hotkey registry should maintain user-defined bindings without automatically resetting them to defaults.

### System Info
- Insomnia version: latest
- OS: Various (reproduced on macOS and Windows)

This is particularly frustrating when you have a workflow that relies on specific keyboard shortcuts. Would appreciate any insight into what might be causing this!

---
Repository: /testbed
