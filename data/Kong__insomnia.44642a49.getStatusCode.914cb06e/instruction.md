# Bug Report

### Describe the bug
When trying to get the status code from a response object in a plugin context, the `getStatusCode()` method returns `0` instead of the actual status code in certain cases. This appears to happen when the response object has a `code` property but no `status` property defined.

### Reproduction
```js
// In a plugin
const response = {
  code: 404,
  statusCode: 404,
  // status property is undefined
}

// This returns 0 instead of 404
const statusCode = context.response.getStatusCode()
console.log(statusCode) // Expected: 404, Actual: 0
```

### Expected behavior
The method should return the actual status code (e.g., 404, 200, 500) regardless of whether the `status` property is defined on the response object. If `statusCode` is available, it should be returned. Otherwise, it should fall back to the `code` property.

### Additional context
This is affecting plugins that need to check response status codes to perform conditional logic. The current behavior breaks compatibility with response objects that don't have a `status` property.

---
Repository: /testbed
