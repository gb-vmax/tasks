# Bug Report

### Describe the bug
OAuth 1.0 authentication is failing when using HMAC-SHA256 or RSA-SHA1 signature methods. The signatures being generated don't match what the API expects, resulting in authentication errors.

### Reproduction
```js
// Using HMAC-SHA256
const oauth1Config = {
  signatureMethod: 'HMAC-SHA256',
  consumerKey: 'my-key',
  consumerSecret: 'my-secret',
  // ... other config
}

// Attempting to authenticate with OAuth 1.0
// Results in signature mismatch errors
```

The same issue occurs with RSA-SHA1 signature method as well.

### Expected behavior
OAuth 1.0 signatures should be calculated correctly and authentication should succeed when using valid credentials.

### Steps to reproduce
1. Configure OAuth 1.0 authentication with HMAC-SHA256 signature method
2. Attempt to make an authenticated request
3. Request fails with signature validation error from the API

This was working fine in previous versions but seems to have broken recently. The generated signatures don't match what the OAuth provider expects.

---
Repository: /testbed
