# Bug Report

### Describe the bug

When using `ProxyConfig.test()` with a URL, the method appears to be broken. The code doesn't compile/run properly and the proxy matching logic is completely non-functional.

### Reproduction

```js
const proxyConfig = new ProxyConfig({
  match: 'http://example.com/*',
  bypass: ['http://example.com/health']
});

// This should work but doesn't
const result = proxyConfig.test('http://example.com/api');
```

### Expected behavior

The `test()` method should:
1. Return `true` when the URL matches the proxy pattern
2. Return `false` when the URL is in the bypass list
3. Handle wildcard patterns correctly in both match and bypass rules

### Additional context

This seems to have broken recently. The proxy configuration is not being applied correctly to requests, and URLs that should be proxied are being bypassed or vice versa.

---
Repository: /testbed
