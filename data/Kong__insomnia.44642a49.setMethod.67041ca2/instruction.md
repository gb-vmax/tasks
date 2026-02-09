# Bug Report

### Describe the bug
After a recent update, the `setMethod()` function in the plugin context is throwing errors when trying to set HTTP methods with lowercase or mixed case strings. Previously, methods like `'get'`, `'post'`, etc. worked fine, but now they're being rejected as invalid.

### Reproduction
```js
// This used to work but now throws an error
request.setMethod('get');
// Error: Invalid HTTP method: "get". Must be one of: GET, POST, PUT, ...

// Same issue with mixed case
request.setMethod('Post');
// Error: Invalid HTTP method: "Post". Must be one of: GET, POST, PUT, ...

// Only uppercase works now
request.setMethod('GET'); // This works
```

### Expected behavior
The plugin should accept HTTP methods in any case (lowercase, uppercase, or mixed case) and normalize them internally. Many plugins and scripts use lowercase method names, so this breaks backward compatibility.

### Additional context
This is breaking existing plugins that were working fine before. The API should be more forgiving and automatically normalize the case rather than requiring exact uppercase matches.

---
Repository: /testbed
