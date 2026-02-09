# Bug Report

### Describe the bug
The save dialog functionality is broken after a recent update. When trying to save a file, the dialog behavior has become inconsistent and the code appears to have syntax errors or malformed structure.

### Reproduction
```js
// Try to show a save dialog
const result = await app.showSaveDialog({
  defaultPath: '/path/to/file.json'
});

// Expected: dialog opens and returns selected path or null
// Actual: code doesn't execute properly
```

### Steps to reproduce:
1. Use the plugin API to call `app.showSaveDialog()`
2. Provide options with a default path
3. The function fails to execute correctly

### Expected behavior
The save dialog should open normally and return either:
- The selected file path if user confirms
- `null` if user cancels

Instead, it looks like there's duplicate or malformed code in the implementation that's preventing it from working at all.

### Additional context
This was working fine in previous versions. Something seems to have gone wrong with the code structure in the `app.tsx` file around the `showSaveDialog` method - there appears to be duplicate or incorrectly merged code.

---
Repository: /testbed
