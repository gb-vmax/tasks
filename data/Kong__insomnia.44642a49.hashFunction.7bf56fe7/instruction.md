# Bug Report

### Describe the bug

OAuth 1.0 authentication is failing with RSA-SHA1 signature method. The authentication request gets rejected by the server with an invalid signature error.

### Reproduction

```js
const oauth1Config = {
  signatureMethod: 'RSA-SHA1',
  consumerKey: 'my-consumer-key',
  consumerSecret: 'my-consumer-secret',
  privateKey: '-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----'
}

// Try to authenticate with RSA-SHA1
// Server responds with 401 - invalid signature
```

### Expected behavior

The OAuth 1.0 request should be signed correctly using RSA-SHA1 and the server should accept the authentication.

### Additional context

This was working fine in previous versions. It seems like the signature generation might not be including the base string properly. I've verified that my private key is correct and the same configuration works with other OAuth clients.

Also noticed some odd behavior with PLAINTEXT signature method where extra data seems to be appended to the signature, but that's less critical for my use case.

---
Repository: /testbed
