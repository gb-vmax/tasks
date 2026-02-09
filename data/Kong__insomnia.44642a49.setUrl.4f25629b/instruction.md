# Bug Report

### Describe the bug

When using the `setUrl()` method in a plugin context, setting a URL with query parameters causes unexpected behavior. The query parameters from the URL are being automatically extracted and added to the request's parameters array, even if they already exist or if the user doesn't want them separated.

### Reproduction

```js
// In a plugin
request.setUrl('https://api.example.com/endpoint?key=value&foo=bar');

// Expected: URL is set to 'https://api.example.com/endpoint?key=value&foo=bar'
// Actual: URL is set to 'https://api.example.com/endpoint' 
//         and parameters array is modified with extracted query params
```

This is problematic when:
1. You want to keep query parameters in the URL string itself
2. The parameters already exist in the parameters array and you end up with duplicates
3. You're working with a URL format that shouldn't have its query string automatically parsed

### Expected behavior

The `setUrl()` method should simply set the URL as provided without automatically parsing and extracting query parameters. If users want to manipulate query parameters separately, they should use the dedicated parameter methods.

### System Info
- Insomnia version: latest
- Plugin API context: request

---
Repository: /testbed
