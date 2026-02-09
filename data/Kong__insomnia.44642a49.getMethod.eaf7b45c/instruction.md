# Bug Report

### Describe the bug
When using the plugin context API, the `getMethod()` function is returning normalized/uppercase HTTP methods instead of preserving the original method casing from the request. This breaks compatibility with existing plugins that expect the method to be returned as-is.

### Reproduction
```js
// In a plugin
const method = context.request.getMethod();

// Previously, if the request had method: 'get'
// This would return 'get'

// Now it returns 'GET' (uppercased)
```

### Expected behavior
The `getMethod()` function should return the HTTP method exactly as it was set in the request, without any normalization or transformation. If the request method was lowercase or mixed case, it should be returned that way.

### Additional context
This appears to have changed recently. My plugin was working fine before but now it's breaking because I was comparing the method string directly with lowercase values like `'get'`, `'post'`, etc.

Also noticed that invalid/empty methods now default to `'GET'` which wasn't the case before - this might be intentional but it's a breaking change for plugins that relied on the original behavior.

---
Repository: /testbed
