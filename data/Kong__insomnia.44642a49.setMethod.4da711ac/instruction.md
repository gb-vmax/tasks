# Bug Report

### Describe the bug

When using the plugin API to change the HTTP method on a request, the method is not being normalized to uppercase. This causes issues when the method is set using lowercase or mixed case strings, as HTTP methods should be standardized to uppercase (e.g., 'GET', 'POST', not 'get' or 'Post').

### Reproduction

```js
// In a plugin script
const method = request.getMethod(); // Returns 'GET'
request.setMethod('post'); // Sets method as 'post' instead of 'POST'

// Later when the request is sent, it may be rejected or behave unexpectedly
// because the method is lowercase
```

### Expected behavior

When calling `setMethod()` with any case variation (e.g., 'post', 'Post', 'POST'), the method should be normalized to uppercase ('POST') to comply with HTTP standards. All HTTP methods should be stored and transmitted in uppercase format.

### Additional context

This affects any plugin that programmatically sets request methods. The issue is particularly problematic when:
- Copying methods from external sources that may use lowercase
- Dynamically generating requests based on user input
- Integrating with APIs that return method names in lowercase

The current implementation just sets whatever string is passed without any normalization.

---
Repository: /testbed
