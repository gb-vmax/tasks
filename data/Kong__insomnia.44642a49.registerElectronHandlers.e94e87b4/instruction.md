# Bug Report

### Describe the bug

I'm experiencing an issue with the menu bar visibility toggle in Electron. When I try to hide the menu bar, it actually becomes visible instead, and when I try to show it, it gets hidden. The behavior is completely inverted from what's expected.

### Reproduction

Steps to reproduce:
1. Open the application
2. Try to hide the menu bar using the visibility toggle
3. The menu bar remains visible (or becomes visible if it was hidden)
4. Try to show the menu bar
5. The menu bar gets hidden instead

The auto-hide behavior is also reversed - when I set the menu bar to be visible, it auto-hides, and when I set it to be hidden, it stays permanently visible.

### Expected behavior

When toggling menu bar visibility:
- Setting visibility to `false` should hide the menu bar
- Setting visibility to `true` should show the menu bar
- The auto-hide behavior should match the visibility setting (hidden = auto-hide enabled, visible = auto-hide disabled)

### System Info
- Insomnia version: latest
- OS: Windows/macOS/Linux
- Electron version: latest

---
Repository: /testbed
