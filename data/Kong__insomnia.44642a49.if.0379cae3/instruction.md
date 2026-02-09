# Bug Report

### Describe the bug
When using proxy authentication with special characters in the username or password, the proxy URL is not being constructed correctly. The credentials are not URL-encoded, which causes issues when connecting through proxies that require authentication with special characters like `@`, `:`, or other reserved URL characters.

Additionally, the proxy URL is missing the protocol prefix (e.g., `http://` or `https://`), which may cause connection failures with certain proxy configurations.

### Reproduction
```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user@domain',
  password: 'p@ss:word'
});

const proxyUrl = proxyConfig.getProxyUrl();
console.log(proxyUrl);
// Current output: user@domain:p@ss:word@proxy.example.com:8080
// This is malformed because the @ and : in credentials are not encoded
```

### Expected behavior
The proxy URL should properly encode special characters in the username and password, and include the appropriate protocol prefix:
```
http://user%40domain:p%40ss%3Aword@proxy.example.com:8080
```

Without proper encoding, the proxy URL becomes ambiguous and cannot be parsed correctly by HTTP clients.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

---
Repository: /testbed
