# Bug Report

### Describe the bug
OAuth 1.0 authentication is failing with HMAC-SHA1 signature method. The requests are being rejected by the server with signature mismatch errors even though all the credentials and parameters appear to be correct.

### Reproduction
```js
const auth = {
  signatureMethod: 'HMAC-SHA1',
  consumerKey: 'my-consumer-key',
  consumerSecret: 'my-consumer-secret',
  tokenKey: 'my-token-key',
  tokenSecret: 'my-token-secret'
}

// Make a request with OAuth 1.0 authentication
// Server returns: "Invalid signature" error
```

### Expected behavior
The OAuth 1.0 signature should be calculated correctly and the request should be authenticated successfully by the server.

### Additional context
This was working fine in previous versions. Started seeing authentication failures after a recent update. The same credentials work when tested with other OAuth 1.0 clients, so the issue seems to be with how the signature is being generated.

---
Repository: /testbed
