# Bug Report

### Describe the bug

After a recent update, the `app.alert()` plugin API seems to be broken. When I call `app.alert()` from my plugin, the alert dialog doesn't appear at all. The function returns a promise that resolves, but no UI is shown to the user.

### Reproduction

```js
module.exports.requestHooks = [
  context => {
    context.app.alert('Test Alert', 'This should show a dialog');
  }
];
```

### Expected behavior

The alert dialog should be displayed with the title "Test Alert" and message "This should show a dialog". Previously this was working fine, but now the dialog just doesn't appear.

### Additional context

I noticed this started happening after updating to the latest version. The promise returned by `alert()` resolves successfully, so it seems like the function thinks it's working, but nothing actually shows up on screen.

This is breaking several of my plugins that rely on showing alerts to users for important notifications.

---
Repository: /testbed
