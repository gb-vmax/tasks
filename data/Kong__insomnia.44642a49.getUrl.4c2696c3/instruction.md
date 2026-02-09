# Bug Report

### Describe the bug

The `getUrl()` method in the plugin context is returning incorrect/truncated URLs. Instead of returning the full URL, it seems to be applying some unexpected string manipulation that removes parts of the URL.

### Reproduction

```js
// When using the request context in a plugin
const url = context.request.getUrl();

// Example 1: URL with query parameters
// Expected: "https://api.example.com/users?id=123"
// Actual: Returns something like "/users?id=123" or partial URL

// Example 2: Simple URL without query params
// Expected: "https://api.example.com/users/profile"
// Actual: Returns "/profile" or just the last segment
```

### Expected behavior

`getUrl()` should return the complete rendered URL including the protocol, domain, path, and query parameters. The full URL should be preserved as-is without any truncation.

### System Info

Using the latest version of Insomnia. This affects plugin development where we need to access the full request URL.

---
Repository: /testbed
