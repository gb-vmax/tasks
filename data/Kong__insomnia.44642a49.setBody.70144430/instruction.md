# Bug Report

### Describe the bug

When using the plugin API to set a response body with `setBody()`, the function is trying to automatically detect and set content encoding headers based on the body content. However, the `detectBodyEncoding` function is being defined outside of the `setBody` method scope, which breaks the code structure and causes a syntax error.

### Reproduction

```js
// In a plugin context
const response = context.response;

// Try to set a response body
const body = Buffer.from('test data');
response.setBody(body);
```

The code will fail to execute due to improper function definition placement.

### Expected behavior

The `setBody()` method should successfully write the body to the file system and update the response metadata without syntax errors. The function should be properly structured with helper functions defined in the correct scope.

### Additional context

This appears to be related to response body manipulation in the plugin context. The issue prevents any plugin from being able to use the `setBody()` functionality at all.

---
Repository: /testbed
