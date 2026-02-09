# Bug Report

### Describe the bug

The plugin API's `app.alert()` function is not working correctly after a recent update. When calling the alert method with a simple title and message, I'm getting unexpected behavior - the function seems to be treating the message parameter in a way that breaks the basic usage pattern.

### Reproduction

```js
// Basic alert usage that should work
app.alert('Error', 'Something went wrong');

// This used to work fine but now the message parameter
// is being processed incorrectly
```

The alert function appears to be trying to parse the message parameter as if it could be an object, but when you pass a simple string message, it doesn't handle it properly.

### Expected behavior

Calling `app.alert(title, message)` with two string parameters should display an alert dialog with the given title and message, just like it did before.

### System Info
- Insomnia version: latest
- OS: Various

This seems like a regression from the previous behavior where you could just pass two strings to show a simple alert. The new implementation looks like it's trying to support additional options but broke the basic use case in the process.

---
Repository: /testbed
