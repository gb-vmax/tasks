# Bug Report

### Describe the bug

The alert modal is not displaying properly when multiple alerts are triggered in quick succession. When I try to show a second alert while the first one is still visible, the second alert doesn't appear at all. It seems like the modal is just ignoring subsequent show() calls if there's already an alert being displayed.

### Reproduction

```js
// Show first alert
alertModal.show({
  title: 'First Alert',
  message: 'This is the first alert',
});

// Immediately try to show second alert
alertModal.show({
  title: 'Second Alert', 
  message: 'This should appear after the first',
});
```

### Expected behavior

The second alert should either:
1. Queue up and display after the first alert is dismissed, or
2. Replace the first alert immediately

Currently, the second alert just disappears and never shows up.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
