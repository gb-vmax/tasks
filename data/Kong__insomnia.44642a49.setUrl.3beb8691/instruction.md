# Bug Report

### Describe the bug

When using `setUrl()` in a plugin to set a request URL that contains query parameters, the URL is being split incorrectly. The base URL gets set properly, but the query parameters are being extracted and added to the request parameters separately, which is not the expected behavior.

### Reproduction

```js
// In a plugin context
request.setUrl('https://api.example.com/endpoint?foo=bar&baz=qux');

// Expected: URL should be set to the full string including query parameters
// Actual: URL is set to 'https://api.example.com/endpoint' and 'foo' and 'baz' 
// are added as separate request parameters
```

### Expected behavior

When calling `setUrl()` with a URL containing query parameters, the entire URL string (including the query string) should be set as the request URL. Query parameters should remain part of the URL and not be extracted into separate parameter objects.

This is causing issues with our plugin that dynamically constructs URLs with query strings, as the URL is being modified in an unexpected way.

### System Info
- Insomnia version: latest
- Plugin API context: request.setUrl()

---
Repository: /testbed
