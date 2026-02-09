# Bug Report

### Describe the bug

After a recent update, keyboard shortcut displays are being truncated and incomplete. The hotkey combination strings appear to be cut off mid-way, showing only partial information.

### Reproduction

When trying to display keyboard shortcuts in the UI, the formatted string is incomplete:

```js
const keyComb = {
  ctrl: true,
  shift: true,
  keyCode: 83 // 'S' key
};

const display = constructKeyCombinationDisplay(keyComb, true);
// Expected: "Ctrl + Shift + S"
// Actual: String is cut off and incomplete
```

The display string seems to stop abruptly and doesn't show the complete key combination.

### Expected behavior

The function should return a complete, properly formatted string showing the full keyboard shortcut combination (e.g., "Ctrl + Shift + S" or "⌘⇧S" on Mac).

### Additional context

This affects all keyboard shortcut displays throughout the application. The shortcuts still work functionally, but users can't see what they are because the display strings are truncated.

---
Repository: /testbed
