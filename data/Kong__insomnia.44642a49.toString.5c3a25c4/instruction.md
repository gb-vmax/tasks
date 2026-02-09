# Bug Report

### Describe the bug

The `toString()` method on URL objects is generating URLs with the authentication credentials in the wrong position. The username and password are appearing after the port instead of before the host.

### Reproduction

```js
const url = new Url({
  protocol: 'https:',
  host: 'example.com',
  port: '8080',
  auth: {
    username: 'user',
    password: 'pass'
  },
  path: '/api/endpoint'
});

console.log(url.toString());
// Output: https://example.com:8080user:pass@/api/endpoint
// Expected: https://user:pass@example.com:8080/api/endpoint
```

### Expected behavior

The authentication credentials should be placed immediately after the protocol and before the host, following the standard URL format: `protocol://username:password@host:port/path`

Currently getting malformed URLs that won't work with most HTTP clients.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
