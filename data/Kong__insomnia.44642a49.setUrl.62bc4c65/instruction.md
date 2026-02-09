# Bug Report

### Describe the bug

When setting a URL through the plugin context's `setUrl()` method, the URL is being unexpectedly modified. The function appears to be normalizing and encoding the URL automatically, which breaks URLs that are intentionally formatted in a specific way or contain special characters.

### Reproduction

```js
// In a plugin script
const url = 'https://example.com//api//endpoint';
request.setUrl(url);
// Expected: https://example.com//api//endpoint
// Actual: URL gets normalized with double slashes removed

// Another case with query parameters
const urlWithParams = 'https://api.example.com/search?q=hello world&type=exact';
request.setUrl(urlWithParams);
// The spaces and special characters get encoded even if not intended
```

### Expected behavior

The `setUrl()` method should set the URL exactly as provided without automatic normalization or encoding. If URL processing is needed, it should be opt-in or configurable rather than applied by default.

This is causing issues with:
- APIs that use double slashes intentionally in their paths
- Pre-encoded URLs getting double-encoded
- URLs that need to preserve their exact format for specific use cases

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
