# Bug Report

### Describe the bug

When using the plugin API to get a request name with `request.getName()`, the method returns the raw template string without processing any variable substitutions. Environment variables and template tags in the request name (like `{{variable_name}}`) are not being rendered/substituted with their actual values.

### Reproduction

```js
// Request name is set to: "API Request - {{environment}}"
// Environment variable "environment" is set to: "production"

const requestName = context.request.getName();
console.log(requestName);
// Expected: "API Request - production"
// Actual: "API Request - {{environment}}"
```

### Expected behavior

The `getName()` method should return the request name with all variables and template tags substituted with their actual values, similar to how other plugin context methods handle variable rendering.

### Additional context

Other methods in the request context appear to handle variable substitution correctly (e.g., `getUrl()`), but `getName()` returns the unprocessed template string.

---
Repository: /testbed
