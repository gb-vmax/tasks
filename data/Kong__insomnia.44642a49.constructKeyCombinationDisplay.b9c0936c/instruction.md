# Bug Report

### Describe the bug

After a recent update, the hotkey display is showing duplicate key combinations when rendering keyboard shortcuts. The display appears to be rendering the keys twice - once with the new formatting and once with the old formatting logic.

### Reproduction

When trying to display a keyboard shortcut combination (like Cmd+Shift+K on Mac or Ctrl+Shift+K on Windows), the output shows the keys repeated or displays incorrectly formatted strings.

Steps to reproduce:
1. Create a key combination with modifiers (e.g., ctrl, shift) and a regular key
2. Call `constructKeyCombinationDisplay()` with `mustUsePlus: true`
3. Observe the output

### Expected behavior

The function should return a single, properly formatted key combination string like "Control + Shift + K" or "⌃⇧K" depending on the platform and display mode. Instead, it seems to be processing the keys multiple times.

### System Info
- Platform: macOS
- Version: Latest from main branch

---
Repository: /testbed
