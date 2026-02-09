# Bug Report

### Describe the bug

I'm experiencing an issue with cookie handling when a cookie has an expiration time of `0`. The cookie appears to be treated as if it has no expiration date instead of being recognized as an expired/session cookie.

### Reproduction

```js
const cookieJar = {
  name: 'test-jar',
  cookies: [
    {
      id: '1',
      key: 'session_id',
      value: 'abc123',
      expires: 0, // Unix epoch time (Jan 1, 1970)
      domain: 'example.com',
      path: '/',
      secure: false,
      httpOnly: true,
      hostOnly: false,
      creation: Date.now(),
      creationIndex: 0,
      lastAccessed: Date.now(),
      pathIsDefault: false
    }
  ]
};

const cookieObject = new CookieObject(cookieJar);
// The cookie with expires: 0 is not being processed correctly
```

### Expected behavior

When a cookie has `expires: 0`, it should be converted to `new Date(0)` which represents the Unix epoch (January 1, 1970). This is a valid expiration date and indicates the cookie should be treated as expired.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
