# Bug Report

### Describe the bug

When using the plugin API to get the HTTP method of a request, `getMethod()` is returning `undefined` for standard HTTP methods like GET, POST, PUT, DELETE, and PATCH. This breaks existing plugins that rely on retrieving the request method.

### Reproduction

```js
// In a plugin's request hook
const method = context.request.getMethod();
console.log(method); // Expected: 'GET', 'POST', etc.
                     // Actual: undefined
```

### Expected behavior

`getMethod()` should return the actual HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE', 'PATCH') for the request, not `undefined`. Plugins need to be able to read the request method to perform conditional logic based on the HTTP verb being used.

### Additional context

This seems to have broken after a recent change. Previously, `getMethod()` would correctly return the request method. Now it only returns a value for non-standard HTTP methods, which doesn't make sense for most use cases.

---
Repository: /testbed
