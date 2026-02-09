# Bug Report

### Describe the bug
After a recent update, the `getMethod()` function in the plugin context is returning HTTP methods in lowercase format instead of uppercase. This is breaking plugins that expect the standard uppercase format (e.g., 'GET', 'POST', 'PUT').

### Reproduction
```js
// In a plugin context
const method = context.request.getMethod();
console.log(method); // Returns 'get' instead of 'GET'

// This comparison now fails
if (method === 'GET') {
  // This block is never executed
}
```

### Expected behavior
The `getMethod()` function should return HTTP methods in uppercase format as per HTTP specification standards (GET, POST, PUT, DELETE, etc.), not lowercase.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with existing plugins that rely on standard HTTP method casing for comparisons and logic.

---
Repository: /testbed
