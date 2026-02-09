# Bug Report

### Describe the bug

The `getProxyUrl()` method in `ProxyConfig` is returning malformed proxy URLs. When authentication is enabled, the URL is missing the protocol prefix (e.g., `http://`, `https://`, `socks5://`), which causes connection failures.

### Reproduction

```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user',
  password: 'pass'
});

const url = proxyConfig.getProxyUrl();
console.log(url);
// Currently returns: "user:pass@proxy.example.com:8080"
// Expected: "http://user:pass@proxy.example.com:8080"
```

### Expected behavior

The proxy URL should include the appropriate protocol prefix based on the configured protocols. For example:
- If protocol is `http`, should return `http://user:pass@proxy.example.com:8080`
- If protocol is `https`, should return `https://user:pass@proxy.example.com:8080`
- If protocol is `socks5`, should return `socks5://user:pass@proxy.example.com:8080`

Without the protocol prefix, proxy clients cannot determine how to connect to the proxy server.

### Additional context

This affects all proxy configurations that use authentication. Non-authenticated proxies also don't include the protocol prefix but may work in some cases where the client defaults to http.

---
Repository: /testbed
