# Bug Report

### Describe the bug
When using the plugin API to set a request URL that ends with a trailing slash, the last character gets incorrectly removed instead of just the trailing slash. URLs ending with `/` are being truncated by 2 characters instead of 1.

### Reproduction
```js
// In a plugin
request.setUrl('https://example.com/api/');
// Expected: https://example.com/api
// Actual: https://example.com/ap

request.setUrl('https://example.com/test/');
// Expected: https://example.com/test
// Actual: https://example.com/tes
```

### Expected behavior
When calling `setUrl()` with a URL ending in a trailing slash, only the trailing slash should be removed, not an additional character.

### Additional context
This seems to affect any URL with a trailing slash. URLs without trailing slashes work fine. Also noticed that URLs containing `#` or `?` are now being silently ignored, which might be related but I'm not sure if that's intentional.

---
Repository: /testbed
