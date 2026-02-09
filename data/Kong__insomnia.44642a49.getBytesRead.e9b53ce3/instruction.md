# Bug Report

### Describe the bug

The `getBytesRead()` method in the response context is returning incorrect values. When a response has bytes read, it returns 0 instead of the actual byte count. This breaks any plugins or scripts that rely on checking the response size.

### Reproduction

```js
// After making a request with a response body
const bytesRead = await context.response.getBytesRead();

// Expected: actual number of bytes (e.g., 1234)
// Actual: always returns 0 when there are bytes read
```

### Expected behavior

`getBytesRead()` should return the actual number of bytes read from the response. If the response has `bytesRead` set to a positive number, that value should be returned. Only when `bytesRead` is undefined/null should it default to 0.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
