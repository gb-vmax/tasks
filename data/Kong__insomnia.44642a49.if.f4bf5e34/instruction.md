# Bug Report

### Describe the bug

I'm experiencing an issue with proxy configuration resolution where the code appears to be duplicated or malformed. When trying to resolve proxy configurations for URLs, the behavior is inconsistent and the method doesn't seem to execute properly.

### Reproduction

```js
const proxyList = new ProxyConfigList();

// Add some proxy configurations
proxyList.add({
  match: 'http://example.com/*',
  host: 'proxy1.com',
  port: 8080
});

proxyList.add({
  match: 'http://example.com/api/*',
  host: 'proxy2.com',
  port: 8080
});

// Try to resolve a URL
const url = new Url('http://example.com/api/users');
const resolved = proxyList.resolve(url);

// Expected: Should return the most specific matching proxy config
// Actual: Unexpected behavior or error
```

### Expected behavior

The `resolve()` method should properly match the URL against configured proxy patterns and return the most appropriate proxy configuration. More specific patterns (like `/api/*`) should take precedence over less specific ones (like `/*`).

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

The issue seems to have appeared recently, possibly after some refactoring of the proxy resolution logic. The method structure looks odd with what appears to be duplicate code or incorrectly placed method definitions.

---
Repository: /testbed
