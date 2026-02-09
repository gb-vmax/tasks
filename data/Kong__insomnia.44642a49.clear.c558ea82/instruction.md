# Bug Report

### Describe the bug

After a recent update, the clipboard `clear()` method is causing syntax errors in the plugin context. The application fails to load properly and throws parsing errors related to the clipboard functionality.

### Reproduction

```js
// Using the plugin API's clipboard context
app.clipboard.writeText('some text');
app.clipboard.clear(); // This causes the app to fail
```

The issue appears when trying to use the clipboard clear functionality through the plugin context API.

### Expected behavior

The `clear()` method should successfully clear the clipboard without causing any errors. The application should continue to function normally after calling this method.

### System Info
- Insomnia version: Latest
- OS: Multiple platforms affected

---
Repository: /testbed
