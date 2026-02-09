# Bug Report

### Describe the bug

After a recent update, the hotkey display functionality appears to be broken. When trying to display keyboard shortcuts in the UI, I'm getting duplicate output or the function seems to execute twice, resulting in malformed hotkey strings.

### Reproduction

When constructing key combination displays with modifier keys, the output contains duplicated elements. For example:

```js
const keyComb = {
  ctrl: true,
  alt: true,
  shift: false,
  meta: false,
  keyCode: 13 // Enter key
};

const display = constructKeyCombinationDisplay(keyComb, true, false);
// Expected: "Ctrl + Alt + Enter"
// Getting: Something like "Ctrl + Alt + Ctrl + Alt + Enter" or similar duplication
```

### Steps to reproduce

1. Create a key combination with multiple modifiers
2. Call `constructKeyCombinationDisplay()` with the combination
3. Observe that the resulting string contains duplicated modifier keys or the entire combination is repeated

### Expected behavior

The function should return a clean, properly formatted hotkey string without any duplication. Each modifier and key should appear exactly once in the correct order.

### System Info

- Platform: Cross-platform (affects both Mac and Windows)
- Version: Latest main branch

This seems to have started happening recently, possibly after refactoring the key display logic. The hotkey strings are being used throughout the UI for showing keyboard shortcuts to users, so this is affecting the user experience.

---
Repository: /testbed
