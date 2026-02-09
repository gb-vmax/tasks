# Bug Report

### Describe the bug

After a recent update, keyboard shortcuts are displaying incorrectly in the UI. The hotkey display function appears to be processing the key combination twice, resulting in duplicated or malformed output.

### Reproduction

When constructing keyboard shortcut displays, the function seems to be executing the logic multiple times. For example:

```js
const keyComb = {
  ctrl: true,
  shift: true,
  keyCode: 83 // 'S' key
};

const display = constructKeyCombinationDisplay(keyComb, true);
// Expected: "Ctrl + Shift + S"
// Actual: Garbled or duplicated output
```

### Expected behavior

The `constructKeyCombinationDisplay` function should return a properly formatted string representing the key combination, with modifiers and keys displayed in the correct order without duplication.

### System Info
- Insomnia version: latest
- OS: macOS / Windows / Linux

The issue seems to affect all platforms. The hotkey display logic appears to have duplicate code paths that are both executing.

---
Repository: /testbed
