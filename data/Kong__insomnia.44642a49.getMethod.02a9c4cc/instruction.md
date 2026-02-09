# Bug Report

### Describe the bug

After a recent update, the `getMethod()` function in the request context is always returning uppercase HTTP methods, even when the original method was set in lowercase or mixed case. This breaks existing plugins that rely on case-sensitive method names or expect to receive the method exactly as it was set.

### Reproduction

```js
// In a plugin using the request context
const request = context.request;

// Set method with lowercase
request.setMethod('get');

// This now returns 'GET' instead of 'get'
const method = request.getMethod();
console.log(method); // Expected: 'get', Actual: 'GET'
```

### Expected behavior

The `getMethod()` function should return the HTTP method exactly as it was set, preserving the original case. If normalization is needed, it should be done elsewhere or made optional.

### Additional context

This is causing issues with plugins that:
- Compare method strings using strict equality
- Store or log methods with specific casing conventions
- Use the method value in case-sensitive APIs

The behavior change appears to be unintentional since `setMethod()` doesn't perform any case normalization when setting the value, but `getMethod()` now always returns uppercase.

---
Repository: /testbed
