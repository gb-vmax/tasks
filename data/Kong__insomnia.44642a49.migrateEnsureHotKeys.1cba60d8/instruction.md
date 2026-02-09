# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard shortcuts where multiple actions can be assigned the same key combination, causing conflicts. When I customize hotkeys and accidentally set two different actions to the same key combo (like Ctrl+S for both "Save" and "Send Request"), both shortcuts remain in the registry and the behavior becomes unpredictable.

### Reproduction

1. Open settings and customize keyboard shortcuts
2. Set action A to use `Ctrl+S`
3. Set action B to also use `Ctrl+S`
4. Both actions now have the same key combination in the registry
5. Pressing `Ctrl+S` triggers inconsistent behavior

The system should detect when the same key combination is assigned to multiple actions and handle this appropriately, but currently it allows duplicate key combos to exist in the hotkey registry.

### Expected behavior

When a key combination conflict is detected (e.g., two actions mapped to the same keys), the system should resolve the conflict automatically. This could be done by:
- Resetting one of the conflicting shortcuts to its default value
- Preventing the duplicate assignment in the first place
- Clearing the conflicting shortcut

### Additional context

This becomes especially problematic after importing settings from another machine or restoring from a backup, where hotkey conflicts might not be immediately obvious. The app continues to function but keyboard shortcuts don't work as expected.

---
Repository: /testbed
