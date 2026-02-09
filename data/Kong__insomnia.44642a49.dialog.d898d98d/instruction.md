# Bug Report

### Describe the bug

When using the plugin API's `app.dialog()` method without the `actions` option, the dialog doesn't display properly anymore. The dialog appears to not render at all or behaves unexpectedly.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const { app } = context;
    
    // Create a simple dialog without actions
    const body = document.createElement('div');
    body.textContent = 'This is a simple message';
    
    app.dialog('My Dialog', body, {
      tall: true
    });
  }
];
```

### Expected behavior

The dialog should display normally with the title "My Dialog" and the body content, just like it did before. Simple dialogs without custom actions should still work.

### Additional context

This seems to have broken recently. Dialogs with the `actions` option might work fine, but basic dialogs without any actions specified are not showing up correctly. This affects plugins that just want to display a simple informational message to the user.

---
Repository: /testbed
