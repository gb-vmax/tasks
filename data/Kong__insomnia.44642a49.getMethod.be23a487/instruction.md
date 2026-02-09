# Bug Report

### Describe the bug

The `request.getMethod()` function in the plugin context is now returning HTTP methods in lowercase instead of uppercase. This breaks existing plugins that expect the method to be returned in uppercase format (e.g., `GET`, `POST`, `PUT`).

### Reproduction

```js
// In a plugin template tag or hook
const method = context.request.getMethod();
console.log(method); // Returns 'get' instead of 'GET'

// This comparison now fails
if (method === 'GET') {
  // This code is never executed
}
```

### Expected behavior

The `getMethod()` function should return HTTP methods in uppercase format to maintain consistency with HTTP specifications and backward compatibility with existing plugins.

For example:
- Should return: `GET`, `POST`, `PUT`, `DELETE`
- Currently returns: `get`, `post`, `put`, `delete`

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
