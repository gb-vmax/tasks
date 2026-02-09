# Bug Report

### Describe the bug

When using the `response.getBytesRead()` method in plugin context, it's returning `0` even when the response has actual bytes read data. The method seems to be returning an incorrect value when `bytesRead` is present.

### Reproduction

```js
// In a plugin that accesses response context
const context = await insomnia.response;
const bytesRead = context.getBytesRead();

// Expected: actual bytes read (e.g., 1024, 5000, etc.)
// Actual: always returns 0 even when response has bytesRead data
console.log(bytesRead); // outputs 0 instead of actual value
```

### Expected behavior

The `getBytesRead()` method should return the actual number of bytes read from the response. If a response has `bytesRead` set to something like 1024, the method should return 1024, not 0.

### Additional context

This seems to have broken recently. Previously the method was working correctly and returning the actual bytes read from responses. Now it consistently returns 0 regardless of the actual response size.

---
Repository: /testbed
