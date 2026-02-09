# Bug Report

### Describe the bug
The `app.alert()` plugin API is not showing alert dialogs when called from plugins. The method appears to return immediately without displaying the alert to the user.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    context.app.alert('Test Alert', 'This message should appear');
    // Alert dialog never shows up
  }
];
```

### Steps to reproduce:
1. Create a plugin that calls `context.app.alert()` with a title and message
2. Trigger the plugin (e.g., through a request hook)
3. Observe that no alert dialog appears

### Expected behavior
The alert dialog should be displayed to the user with the provided title and message, similar to how it worked in previous versions.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
