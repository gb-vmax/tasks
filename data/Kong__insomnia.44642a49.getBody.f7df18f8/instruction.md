# Bug Report

### Describe the bug

The `getBody()` method in the response plugin context is not returning the response body correctly. When a response object exists, it appears to be calling `getBodyBuffer()` without passing the response parameter, which likely results in undefined or null being returned instead of the actual response body.

### Reproduction

```js
// In a plugin, trying to access response body
const response = context.response;
const body = response.getBody();

// body is undefined/null even though response exists
console.log(body); // Expected: Buffer with response data, Actual: undefined
```

### Expected behavior

When calling `getBody()` on a response context that has a valid response object, it should return the actual body buffer of that response. The method should properly pass the response object to `getBodyBuffer()` to retrieve the correct data.

### Additional context

This seems to affect any plugin that needs to access response bodies programmatically. The logic appears inverted - when a response exists, it's not being passed to the underlying `getBodyBuffer()` call.

---
Repository: /testbed
