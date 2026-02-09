# Bug Report

### Describe the bug
Cookies with an expiration timestamp of 0 (which represents the Unix epoch: January 1, 1970) are not being handled correctly. When a cookie has `expires: 0`, it should be treated as an expired cookie with a specific expiration date, but instead the expiration is being set to `null`.

### Reproduction
```js
const cookieJar = {
  name: 'test-jar',
  cookies: [{
    id: 'cookie1',
    key: 'session',
    value: 'abc123',
    expires: 0,  // Unix epoch timestamp
    domain: 'example.com',
    path: '/',
    secure: false,
    httpOnly: true,
    hostOnly: false
  }]
};

const cookieObject = new CookieObject(cookieJar);
// The cookie's expires property is null instead of Date(0)
console.log(cookieObject.cookieJar.cookies[0].expires);
// Expected: Date object representing Jan 1, 1970
// Actual: null
```

### Expected behavior
A cookie with `expires: 0` should have its expiration set to `new Date(0)` (the Unix epoch), not `null`. This is a valid timestamp that represents an expired cookie, and should be preserved.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
