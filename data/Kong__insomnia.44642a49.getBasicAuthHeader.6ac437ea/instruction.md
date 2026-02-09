# Bug Report

### Describe the bug
Basic authentication headers are being generated with username and password in the wrong order. When making requests with basic auth, the server rejects the credentials even though they're correct.

### Reproduction
```js
const username = 'myuser';
const password = 'mypass';
const header = getBasicAuthHeader(username, password);

// Expected: Authorization: Basic bXl1c2VyOm15cGFzcw==
// Actual: Authorization: Basic bXlwYXNzOm15dXNlcg==
```

When I decode the base64 string, it shows `mypass:myuser` instead of `myuser:mypass`. The basic auth spec requires the format to be `username:password`, but it appears to be reversed.

### Expected behavior
The authorization header should follow the standard format of `username:password` encoded in base64, not `password:username`.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing authentication failures with any API that uses basic auth. The credentials are correct but the order is swapped in the encoded string.

---
Repository: /testbed
