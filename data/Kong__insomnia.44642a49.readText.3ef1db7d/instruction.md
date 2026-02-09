# Bug Report

### Describe the bug
The plugin API's `clipboard.readText()` method is returning an empty string when an error occurs instead of properly rejecting the promise or propagating the error. This makes it impossible to handle clipboard read failures in plugins.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  async (context) => {
    try {
      const clipboardText = await context.app.clipboard.readText();
      console.log('Clipboard content:', clipboardText);
    } catch (error) {
      // This catch block is never reached even when clipboard access fails
      console.error('Failed to read clipboard:', error);
    }
  }
];
```

When clipboard access is denied or fails for any reason, the method silently returns an empty string instead of throwing an error or rejecting the promise. This makes it impossible to distinguish between:
1. An actual empty clipboard
2. A clipboard read failure due to permissions
3. Any other error that might occur

### Expected behavior
The method should either:
- Reject the promise with an error when clipboard reading fails
- Throw an error that can be caught
- At minimum, provide some way to detect that an error occurred vs. the clipboard actually being empty

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
