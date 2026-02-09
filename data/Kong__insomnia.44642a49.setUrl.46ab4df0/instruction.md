# Bug Report

### Describe the bug

After a recent update, the `setUrl()` method in the plugin context is behaving unexpectedly. When setting a URL with query parameters, the parameters are being automatically extracted and added to the request's parameter collection. This breaks existing plugins that rely on the URL being set exactly as provided.

### Reproduction

```js
// In a plugin's request context
request.setUrl('https://example.com/api?foo=bar&baz=qux');

// Expected: URL is set to 'https://example.com/api?foo=bar&baz=qux'
// Actual: URL is set to 'https://example.com/api' and parameters are extracted separately
```

The issue occurs when:
1. Using `setUrl()` with a URL containing query parameters
2. The query parameters get stripped from the URL
3. The parameters are added to the request's parameter collection instead

### Expected behavior

The `setUrl()` method should set the URL exactly as provided without modifying it or extracting query parameters. If I want to set parameters separately, I should use the parameter-specific methods.

This is breaking backward compatibility with existing plugins that expect the URL to remain unchanged.

### System Info
- Insomnia version: latest
- Plugin API context: request

---
Repository: /testbed
