# Bug Report

### Describe the bug

The keyboard shortcut display is not showing correctly on non-Mac platforms. It appears that the function is returning early before properly handling Windows/Linux modifier key ordering, which causes keyboard shortcuts to not display at all or display incorrectly.

### Reproduction

```js
// On Windows or Linux
const keyCombination = {
  ctrl: true,
  shift: true,
  keyCode: 'KeyS'
};

const display = constructKeyCombinationDisplay(keyCombination);
// Expected: "Ctrl+Shift+S"
// Actual: Returns empty or incomplete string
```

### Steps to reproduce

1. Use the app on Windows or Linux
2. Try to view keyboard shortcuts in the UI
3. Notice that shortcuts are not displayed properly or are missing entirely

### Expected behavior

Keyboard shortcuts should display correctly on all platforms (Windows, Linux, Mac) with proper modifier key ordering and formatting.

### System Info
- OS: Windows 10 / Linux
- Version: Latest

This seems to be affecting all keyboard shortcut displays in the application on non-Mac systems.

---
Repository: /testbed
