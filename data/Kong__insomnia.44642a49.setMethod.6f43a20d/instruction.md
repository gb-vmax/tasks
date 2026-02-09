# Bug Report

### Describe the bug
When using the plugin API to set HTTP methods, the method is being unexpectedly converted to lowercase. This breaks requests that require uppercase HTTP methods (which is the standard convention).

### Reproduction
```js
// In a plugin
request.setMethod('POST');
const method = request.getMethod();
console.log(method); // Expected: 'POST', Actual: 'post'
```

### Steps to reproduce:
1. Use the plugin context API to set a request method
2. Call `request.setMethod('GET')` or any other standard HTTP method
3. Retrieve the method using `request.getMethod()`
4. The method is returned in lowercase instead of uppercase

### Expected behavior
HTTP methods should maintain their case (typically uppercase as per HTTP standards). Setting `'POST'` should return `'POST'`, not `'post'`.

### Additional context
This appears to have started happening recently. HTTP methods are case-sensitive in some contexts and the standard convention is to use uppercase (GET, POST, PUT, DELETE, etc.). Converting them to lowercase could cause issues with servers or tools that expect proper casing.

---
Repository: /testbed
