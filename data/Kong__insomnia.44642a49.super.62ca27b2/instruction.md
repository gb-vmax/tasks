# Bug Report

### Describe the bug

Cookie parsing is broken when passing a string to the Cookie constructor. Valid cookie strings are being rejected with an error while invalid strings are being accepted without error.

### Reproduction

```js
// This should work but throws an error
const cookie1 = new Cookie('sessionId=abc123; Path=/; HttpOnly');

// This should throw an error but doesn't
const cookie2 = new Cookie('invalid cookie string!!!');
```

When creating a Cookie object from a valid cookie string, I'm getting the error "failed to parse cookie, the cookie string seems invalid" even though the string is properly formatted. Meanwhile, passing completely invalid strings doesn't raise any errors at all.

### Expected behavior

Valid cookie strings should be parsed successfully without throwing errors, and invalid cookie strings should throw the error message.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
