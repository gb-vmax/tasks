# Bug Report

### Describe the bug

When using the plugin API to get request URL via `request.getUrl()`, the method returns the entire request object instead of just the URL string when the URL property is undefined or missing. This breaks plugins that expect a string return value.

### Reproduction

```js
// In a plugin context
const url = await context.request.getUrl();

// Expected: url should be a string or undefined
// Actual: url is the entire renderedRequest object when url property is missing
console.log(typeof url); // prints 'object' instead of 'string'
```

### Expected behavior

The `getUrl()` method should consistently return either:
- A string containing the URL when available
- `undefined` when the URL is not set

It should never return the entire request object.

### System Info
- Insomnia version: latest
- Plugin API context: request

---
Repository: /testbed
