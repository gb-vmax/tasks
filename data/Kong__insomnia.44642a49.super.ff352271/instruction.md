# Bug Report

### Describe the bug

When creating a Cookie object from a valid cookie string, it throws an error "failed to parse cookie, the cookie string seems invalid" even though the cookie string is properly formatted. This makes it impossible to initialize cookies from string format.

### Reproduction

```js
// This should work but throws an error
const cookie = new Cookie('sessionId=abc123; Path=/; HttpOnly');
```

The error occurs when passing a valid cookie string to the Cookie constructor. The cookie string parses successfully but still triggers the error message.

### Expected behavior

The Cookie constructor should accept a valid cookie string and create a Cookie object without throwing an error. Only invalid/malformed cookie strings should throw the parsing error.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
