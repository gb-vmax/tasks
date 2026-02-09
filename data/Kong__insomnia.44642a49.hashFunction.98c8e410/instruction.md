# Bug Report

### Describe the bug
OAuth 1.0 authentication is failing when using HMAC-SHA256 signature method. The requests are being rejected with invalid signature errors even though the credentials are correct.

### Reproduction
```js
const oauthConfig = {
  signatureMethod: 'HMAC-SHA256',
  consumerKey: 'valid_key',
  consumerSecret: 'valid_secret',
  tokenKey: 'valid_token',
  tokenSecret: 'valid_token_secret'
}

// Make an OAuth 1.0 request with HMAC-SHA256
// The signature generated is invalid and the request fails
```

### Expected behavior
OAuth 1.0 requests using HMAC-SHA256 signature method should generate valid signatures and authenticate successfully.

### System Info
- Insomnia version: latest
- OS: macOS

This was working fine in previous versions but seems to have broken recently. Other signature methods like HMAC-SHA1 appear to still work correctly.

---
Repository: /testbed
