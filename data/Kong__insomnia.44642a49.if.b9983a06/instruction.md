# Bug Report

### Describe the bug
When using `getProxyUrl()` method from ProxyConfig, the returned URL is missing the protocol scheme prefix (e.g., `http://`, `https://`, `socks5://`). The method currently returns URLs in the format `username:password@host:port` or just `host:port`, which are not valid proxy URLs.

### Reproduction
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user',
  password: 'pass'
});

const proxyUrl = proxyConfig.getProxyUrl();
console.log(proxyUrl);
// Expected: http://user:pass@proxy.example.com:8080
// Actual: user:pass@proxy.example.com:8080
```

Without authentication:
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: false
});

const proxyUrl = proxyConfig.getProxyUrl();
console.log(proxyUrl);
// Expected: http://proxy.example.com:8080
// Actual: proxy.example.com:8080
```

### Expected behavior
The `getProxyUrl()` method should return a complete proxy URL with the appropriate protocol scheme. It should also:
- Support different proxy protocols (http, https, socks4, socks5)
- Properly encode username and password to handle special characters
- Return valid URLs that can be used directly with proxy clients

### Additional context
This affects any code that relies on `getProxyUrl()` to configure proxy settings, as the returned value is not a valid URL format.

---
Repository: /testbed
