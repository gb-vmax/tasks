# Bug Report

### Describe the bug
When calling `getStatusCode()` on a response object that is `null` or `undefined`, the method returns `null`/`undefined` instead of returning a default value like `0`. This breaks code that expects a numeric status code.

### Reproduction
```js
const response = null;
const statusCode = response.getStatusCode();
// statusCode is now null instead of 0
```

When the response is undefined or null, `getStatusCode()` should return a sensible default (like 0) rather than passing through the null/undefined value.

### Expected behavior
The method should return `0` when the response is null or undefined, maintaining backwards compatibility with code that expects a numeric return value.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
