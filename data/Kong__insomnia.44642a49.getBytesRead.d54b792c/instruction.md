# Bug Report

### Describe the bug

After a recent update, the `getBytesRead()` method in the response context is returning an object instead of a number in some cases. This breaks existing plugin code that expects a numeric value.

### Reproduction

```js
// In a plugin's response hook
const response = context.response;
const bytesRead = response.getBytesRead();

// This used to work, but now throws an error
const totalBytes = bytesRead + 1000;
// TypeError: Cannot perform arithmetic on object
```

The method now seems to return either a number or an object depending on some condition, but this isn't documented and breaks backward compatibility with existing plugins.

### Expected behavior

`getBytesRead()` should consistently return a number representing the bytes read, as it did before. If additional information needs to be provided, it should either be through a separate method or the return type should remain consistent.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with several custom plugins that rely on this method for calculating bandwidth metrics.

---
Repository: /testbed
