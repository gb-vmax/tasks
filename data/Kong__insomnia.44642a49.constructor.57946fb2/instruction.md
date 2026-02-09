# Bug Report

### Describe the bug

When creating a `QueryParam` object with a string that looks like JSON but isn't actually valid JSON (e.g., a simple key-value pair like `"key=value"`), the constructor now throws an error instead of parsing it correctly. This breaks existing code that was passing query string formatted parameters.

### Reproduction

```js
// This used to work but now throws an error
const param = new QueryParam("name=value");

// The constructor tries to parse it as JSON because it checks if the string
// starts with '{' and ends with '}', but for regular query string format
// it should use the parseSingle method instead
```

### Expected behavior

The `QueryParam` constructor should be able to handle query string formatted parameters (e.g., `"key=value"`) without throwing an error. It should only attempt JSON parsing when the string is actually JSON-formatted.

### Additional context

This seems to have started happening after a recent change to the constructor logic. The issue appears to be related to how the constructor determines whether to parse the string as JSON or as a query parameter format.

---
Repository: /testbed
