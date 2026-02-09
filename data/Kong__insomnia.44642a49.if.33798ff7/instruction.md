# Bug Report

### Describe the bug
The `getProxyUrl()` method is generating malformed proxy URLs. It's missing the protocol prefix (like `http://` or `https://`) which causes connection failures when trying to use the proxy configuration.

### Reproduction
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: false
});

console.log(proxyConfig.getProxyUrl());
// Currently returns: "proxy.example.com:8080"
// Expected: "http://proxy.example.com:8080"
```

With authentication enabled:
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user',
  password: 'pass'
});

console.log(proxyConfig.getProxyUrl());
// Currently returns: "user:pass@proxy.example.com:8080"
// Expected: "http://user:pass@proxy.example.com:8080"
```

### Expected behavior
The proxy URL should include the protocol scheme (e.g., `http://` or `https://`) at the beginning. Most HTTP clients and proxy libraries expect a fully qualified URL format.

Additionally, when credentials contain special characters, they should be properly URL-encoded to avoid parsing issues.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
