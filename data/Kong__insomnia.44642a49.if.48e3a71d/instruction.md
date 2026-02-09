# Bug Report

### Describe the bug

When using the `showSaveDialog` method in the plugin context, the dialog doesn't appear and the function always returns `null`. The save dialog functionality seems to be completely broken after a recent update.

### Reproduction

```js
const result = await app.showSaveDialog({
  defaultPath: 'export.json'
});

console.log(result); // Always prints null
```

Steps to reproduce:
1. Call `app.showSaveDialog()` from a plugin
2. The dialog should open but doesn't
3. The function immediately returns `null` instead of showing the save dialog

### Expected behavior

The save dialog should open and allow the user to select a file path. The function should return the selected file path or `null` if the user cancels.

### Additional context

This was working fine before, but now it seems like the dialog never gets triggered. I'm not sure if this is related to the `canShowDialogs` check or something else, but the functionality is completely broken for plugins that need to save files.

---
Repository: /testbed
