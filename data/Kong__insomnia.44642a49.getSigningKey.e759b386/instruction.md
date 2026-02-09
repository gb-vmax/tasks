# Bug Report

### Describe the bug
OAuth 1.0 authentication with RSA-SHA1 signature method is failing. When attempting to authorize requests using RSA-SHA1, the signing key is not being generated correctly, causing authentication to fail.

### Reproduction
```js
// Configure OAuth 1.0 with RSA-SHA1
const oauthConfig = {
  signatureMethod: 'RSA-SHA1',
  consumerKey: 'my-key',
  consumerSecret: 'my-secret',
  tokenSecret: 'token-secret'
}

// Try to make an authenticated request
// The request fails with authentication error
```

### Expected behavior
RSA-SHA1 signed OAuth 1.0 requests should authenticate successfully. The signing key should be properly returned for the authorization process.

### System Info
- Version: Latest
- Auth method: OAuth 1.0 with RSA-SHA1

---
Repository: /testbed
