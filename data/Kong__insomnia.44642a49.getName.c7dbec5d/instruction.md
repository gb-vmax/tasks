# Bug Report

### Describe the bug

The `request.getName()` plugin context method is returning incorrect values. Instead of returning the request name as expected, it's returning `undefined` when the request has a name, and returning the entire request object when it doesn't have a name.

### Reproduction

```js
// In a plugin using the request context
module.exports.requestHooks = [
  context => {
    const name = context.request.getName();
    console.log('Request name:', name);
    // Expected: prints the actual request name (e.g., "My API Request")
    // Actual: prints undefined or the entire request object
  }
];
```

### Steps to reproduce:
1. Create a plugin that uses `context.request.getName()`
2. Call the method on a request that has a name set
3. Observe that it returns `undefined` instead of the request name

### Expected behavior

`request.getName()` should return the name of the request as a string when the request has a name property set.

### System Info
- Insomnia version: latest
- OS: N/A

This seems like it might be a recent regression as plugins that previously worked are now failing to get request names properly.

---
Repository: /testbed
