# Bug Report

### Describe the bug

When using `ProxyConfig.getProxyUrl()`, the returned proxy URL is missing the protocol scheme (e.g., `http://`, `https://`, `socks5://`). This causes issues when the proxy URL is used with libraries that expect a fully qualified URL.

### Reproduction

```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: false
});

const url = proxyConfig.getProxyUrl();
console.log(url); // Returns: proxy.example.com:8080
// Expected: http://proxy.example.com:8080
```

With authentication:
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user',
  password: 'pass'
});

const url = proxyConfig.getProxyUrl();
console.log(url); // Returns: user:pass@proxy.example.com:8080
// Expected: http://user:pass@proxy.example.com:8080
```

### Expected behavior

The `getProxyUrl()` method should return a complete proxy URL with the appropriate protocol scheme. It should:
- Detect the protocol from the proxy configuration
- Default to `http://` if no protocol is specified
- Support different proxy types (http, https, socks5)
- Properly encode username and password in the URL

### Additional context

This is causing connection failures when the proxy URL is passed to HTTP clients that require a full URL format.

---
Repository: /testbed
