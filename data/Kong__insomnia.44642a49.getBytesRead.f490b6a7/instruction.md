# Bug Report

### Describe the bug

The `getBytesRead()` method in the response context is returning unexpected values after a recent update. When calling this method without any arguments, it's now returning bandwidth statistics instead of just the total bytes read like it used to.

### Reproduction

```js
// In a plugin's response hook
const bytesRead = response.getBytesRead();
console.log(bytesRead);
// Expected: a number (e.g., 1024)
// Actual: undefined or unexpected value
```

Previously this would return a simple number representing the total bytes read from the response. Now it seems like the method signature changed but the default behavior isn't working as expected.

### Expected behavior

When calling `getBytesRead()` without any parameters, it should return the total number of bytes read as a number, maintaining backwards compatibility with existing plugins.

### System Info
- Insomnia version: latest
- Platform: macOS

This is breaking existing plugins that rely on the simple numeric return value from `getBytesRead()`.

---
Repository: /testbed
