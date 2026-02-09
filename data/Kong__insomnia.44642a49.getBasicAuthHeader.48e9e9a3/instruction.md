# Bug Report

### Describe the bug

Basic authentication headers are being generated incorrectly. The username and password appear to be in the wrong order, and the encoding is not being applied properly.

### Reproduction

```js
const header = getBasicAuthHeader('myuser', 'mypass', 'utf8');
```

When I check the generated Authorization header, the credentials are encoded incorrectly. If I decode the base64 string, I get `mypass:myuser` instead of `myuser:mypass`.

Also, it seems like the encoding parameter is being ignored - regardless of what encoding I pass in, it's always using 'base64' instead of the specified encoding.

### Expected behavior

The Basic auth header should follow the standard format: `username:password` encoded in base64. The encoding parameter should be respected when creating the buffer.

So for username='myuser' and password='mypass', the decoded credentials should be `myuser:mypass`, not `mypass:myuser`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
