# Bug Report

### Describe the bug

When using `setUrl()` in a plugin context, setting a URL with query parameters causes the query parameters to be extracted and added to the request's parameters array. This breaks existing behavior where the full URL (including query string) should be set directly.

### Reproduction

```js
// In a plugin
const url = 'https://api.example.com/endpoint?foo=bar&baz=qux';
context.request.setUrl(url);

// Expected: renderedRequest.url = 'https://api.example.com/endpoint?foo=bar&baz=qux'
// Actual: renderedRequest.url = 'https://api.example.com/endpoint'
//         and query params are added to renderedRequest.parameters array
```

### Expected behavior

The `setUrl()` method should set the complete URL as-is without parsing or modifying query parameters. If I want to set query parameters separately, I should use the parameters API directly.

This is causing issues with URLs that have query strings because:
1. The URL gets truncated at the `?` character
2. Query parameters are unexpectedly added to the parameters collection
3. Existing parameters with the same names are not overwritten (only new ones are added)

### System Info
- Version: Latest from main branch

---
Repository: /testbed
