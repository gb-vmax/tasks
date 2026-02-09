# Bug Report

### Describe the bug

OAuth 1.0 authentication is failing when using HMAC-SHA256 signature method. The requests are being rejected by the server with signature validation errors, even though the credentials are correct.

### Reproduction

1. Set up OAuth 1.0 authentication with signature method set to `HMAC-SHA256`
2. Configure valid consumer key, consumer secret, and tokens
3. Send a request
4. Server returns 401 Unauthorized with signature mismatch error

Example configuration:
```js
{
  signatureMethod: 'HMAC-SHA256',
  consumerKey: 'valid_key',
  consumerSecret: 'valid_secret',
  tokenKey: 'valid_token',
  tokenSecret: 'valid_token_secret'
}
```

### Expected behavior

The OAuth 1.0 signature should be generated correctly using the SHA256 hashing algorithm when `HMAC-SHA256` is selected as the signature method. The server should accept the request with a valid signature.

### Additional context

This seems to have started happening recently. HMAC-SHA1 signature method still works fine, but HMAC-SHA256 consistently fails signature validation. The same credentials work correctly in other OAuth clients.

---
Repository: /testbed
