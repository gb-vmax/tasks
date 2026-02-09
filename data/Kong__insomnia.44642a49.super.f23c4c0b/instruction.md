# Bug Report

### Describe the bug
When creating a Cookie object from a valid cookie string, I'm getting an error saying "failed to parse cookie, the cookie string seems invalid" even though the cookie string is properly formatted.

### Reproduction
```js
const cookieString = 'sessionId=abc123; Path=/; HttpOnly';
const cookie = new Cookie(cookieString);
// Error: failed to parse cookie, the cookie string seems invalid
```

The cookie string is valid and should parse correctly, but instead it throws an error.

### Expected behavior
The Cookie constructor should successfully parse valid cookie strings and create a Cookie object without throwing an error. The error should only be thrown when the cookie string is actually invalid or cannot be parsed.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
