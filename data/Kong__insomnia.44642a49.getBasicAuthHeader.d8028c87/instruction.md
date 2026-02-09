# Bug Report

### Describe the bug

Basic authentication headers are being generated incorrectly. The password appears to be getting double-encoded/decoded in an unexpected way, resulting in authentication failures when trying to connect to APIs that require basic auth.

### Reproduction

```js
const username = 'testuser';
const password = 'mypassword123';

const header = getBasicAuthHeader(username, password);
// The authorization header value is malformed
// Expected: Basic dGVzdHVzZXI6bXlwYXNzd29yZDEyMw==
// Actual: Something completely different
```

When I use this header to authenticate against a server, I get 401 Unauthorized errors even though the credentials are correct. If I manually construct the basic auth header using the standard base64 encoding of `username:password`, it works fine.

### Expected behavior

The `getBasicAuthHeader` function should:
1. Concatenate username and password with a colon separator
2. Base64 encode the resulting string
3. Prepend "Basic " to create the authorization header value

This is the standard way basic auth headers are constructed according to RFC 7617.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
