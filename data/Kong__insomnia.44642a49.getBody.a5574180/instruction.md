# Bug Report

### Describe the bug

When trying to access the response body through the plugin context API, I'm getting incorrect or empty data. The `getBody()` method doesn't seem to be returning the actual response body anymore.

### Reproduction

```js
// In a plugin script
const body = await context.response.getBody();
console.log(body); // Returns unexpected data or throws an error
```

Steps to reproduce:
1. Create a plugin that uses `context.response.getBody()`
2. Make a request that returns a response with a body
3. Try to access the body through the plugin context
4. The body data is incorrect or unavailable

### Expected behavior

The `getBody()` method should return the actual response body buffer from the current response object, allowing plugins to access and process the response data correctly.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently. Previously the response body was accessible without issues through the plugin API.

---
Repository: /testbed
