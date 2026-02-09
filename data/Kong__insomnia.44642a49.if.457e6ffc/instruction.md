# Bug Report

### Describe the bug

When using `ProxyConfig.getProxyUrl()` with authentication, the generated proxy URL is missing the protocol scheme (e.g., `http://` or `https://`). This causes issues when the proxy URL is used with HTTP clients that expect a fully qualified URL.

### Reproduction

```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'myuser',
  password: 'mypass'
});

const proxyUrl = proxyConfig.getProxyUrl();
console.log(proxyUrl);
// Current output: myuser:mypass@proxy.example.com:8080
// Expected output: http://myuser:mypass@proxy.example.com:8080
```

Also, if the username or password contains special characters like `@` or `:`, they're not being URL-encoded, which breaks the proxy URL format.

```js
const proxyConfig = new ProxyConfig({
  host: 'proxy.example.com',
  port: 8080,
  authenticate: true,
  username: 'user@domain',
  password: 'pass:word'
});

const proxyUrl = proxyConfig.getProxyUrl();
// Current output: user@domain:pass:word@proxy.example.com:8080
// This is ambiguous - which @ is the separator?
```

### Expected behavior

The proxy URL should:
1. Include the protocol scheme (http:// or https://)
2. Properly encode special characters in username and password
3. Return a valid proxy URL that can be used directly with HTTP clients

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
