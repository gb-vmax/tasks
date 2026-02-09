# Bug Report

### Describe the bug

The save dialog is broken after a recent change. When trying to save a file using the plugin API's `showSaveDialog()` method, the dialog doesn't appear and the function seems to hang or behave unexpectedly.

### Reproduction

```js
// Using the plugin API
const app = context.app;

// Try to show save dialog
const filePath = await app.showSaveDialog({
  defaultPath: '/some/path/file.json'
});

// Dialog doesn't show up properly
console.log(filePath); // Expected a file path or null
```

### Expected behavior

The save dialog should open normally and allow the user to select a save location. The function should return the selected file path or null if the user cancels.

### Additional context

This was working fine before. The dialog either doesn't appear at all or the function returns unexpected results. It seems like something might be wrong with how the dialog options are being handled or passed through.

---
Repository: /testbed
