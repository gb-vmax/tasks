# Bug Report

### Describe the bug

The plugin alert dialog is not showing up when called through the plugin API. The `app.alert()` method seems to resolve immediately without displaying any dialog to the user.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    context.app.alert('Test Alert', 'This message should be displayed');
  }
];
```

### Expected behavior

When `app.alert()` is called, a dialog should appear with the title and message. Instead, the method returns immediately and no dialog is shown.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The alert dialogs were working fine before.

---
Repository: /testbed
