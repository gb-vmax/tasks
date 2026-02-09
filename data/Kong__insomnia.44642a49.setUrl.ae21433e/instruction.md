# Bug Report

### Describe the bug

When using `setUrl()` in a plugin to update a request URL, the original URL gets modified unexpectedly. If the URL contains query parameters, they are being stripped from the URL and the base URL is set without them. This breaks workflows where we need to set a complete URL including query parameters.

### Reproduction

```js
// In a plugin
const url = 'https://api.example.com/endpoint?foo=bar&baz=qux';
request.setUrl(url);

// Expected: request.url = 'https://api.example.com/endpoint?foo=bar&baz=qux'
// Actual: request.url = 'https://api.example.com/endpoint'
// The query parameters are missing from the URL
```

### Expected behavior

The `setUrl()` method should set the complete URL as provided, including any query parameters. The URL should remain intact and not be modified or split apart.

### System Info

- Insomnia version: latest
- Platform: All platforms

This appears to have started happening recently. Previously, calling `setUrl()` would just set the URL directly without any modifications.

---
Repository: /testbed
