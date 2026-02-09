# Bug Report

### Describe the bug

The `ProxyConfig.test()` method is returning incorrect results when checking if a URL should use the proxy. It seems like the logic for handling URLs has been inverted - when I provide a valid URL, it always returns `false` even when the URL should be proxied.

### Reproduction

```js
const proxyConfig = new ProxyConfig({
  server: 'proxy.example.com',
  port: 8080,
  bypass: []
});

// This should return true (URL should use proxy)
// but it returns false instead
const result = proxyConfig.test('https://api.example.com');
console.log(result); // Expected: true, Actual: false
```

### Expected behavior

When calling `test()` with a URL that is not in the bypass list, it should return `true` to indicate the URL should be proxied. Currently it's returning `false` for all valid URLs.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
