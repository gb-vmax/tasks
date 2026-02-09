# Bug Report

### Describe the bug

The `request.getUrl()` function in the plugin context is not returning the complete URL with query parameters. When trying to access the full URL including query parameters from a plugin, only the base URL is returned, which breaks plugins that need to work with the complete request URL.

### Reproduction

```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const url = context.request.getUrl();
    // url only contains base URL like "https://api.example.com/endpoint"
    // but expected "https://api.example.com/endpoint?param1=value1&param2=value2"
  }
];
```

When a request has query parameters defined in Insomnia, the `getUrl()` method doesn't include them in the returned URL string. This makes it difficult to work with the actual request URL that will be sent.

### Expected behavior

The `getUrl()` method should return the complete URL including query parameters, or there should be a way to optionally include them (e.g., `getUrl(true)` or similar).

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with plugins that need to log or modify the complete request URL. Any workaround would be appreciated!

---
Repository: /testbed
