# Bug Report

### Describe the bug

When calling `getStatusCode()` on a response context in a plugin, it returns `undefined` instead of `0` when there's no status code available. This breaks existing plugins that expect a numeric value (specifically `0`) to indicate a missing or failed response.

### Reproduction

```js
// In a plugin's response hook
module.exports.responseHooks = [
  context => {
    const statusCode = context.response.getStatusCode();
    
    // This now fails when there's no response
    if (statusCode === 0) {
      console.log('No response received');
    }
    
    // statusCode is now undefined instead of 0
    console.log(statusCode); // Expected: 0, Actual: undefined
  }
];
```

### Expected behavior

`getStatusCode()` should return `0` when no status code is available, maintaining backward compatibility with existing plugins that check for `statusCode === 0` to detect failed or missing responses.

### System Info
- Insomnia version: latest
- Platform: All

This appears to be a breaking change that affects plugin compatibility.

---
Repository: /testbed
