# Bug Report

### Describe the bug

When using the plugin API's `request.setMethod()` function, the HTTP method isn't being normalized properly. I'm passing in lowercase method names like `'get'` or `'post'`, but the request is being sent with the lowercase value instead of being converted to uppercase.

Also, when changing a request method to GET, the request body is still being included in the request, which causes issues with some servers that reject GET requests with bodies.

### Reproduction

```js
// In a plugin
const method = 'get'; // lowercase
context.request.setMethod(method);

// Expected: method should be 'GET' (uppercase)
// Actual: method remains 'get' (lowercase)

// Also, if there was a body set previously:
context.request.setMethod('GET');
// Expected: body should be cleared for GET request
// Actual: body is still present
```

### Expected behavior

1. HTTP methods should be automatically normalized to uppercase (GET, POST, PUT, etc.)
2. When setting method to GET, HEAD, DELETE, or other bodiless methods, the request body should be automatically cleared
3. Invalid or empty method values should default to 'GET'

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
