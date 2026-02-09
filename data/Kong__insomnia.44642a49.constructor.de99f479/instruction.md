# Bug Report

### Describe the bug

The `CookieObject` constructor is broken after a recent change. When trying to instantiate a `CookieObject` with a cookie jar, I'm getting errors because the constructor implementation appears to be incomplete.

### Reproduction

```js
const cookieJar = {
  name: 'test-jar',
  cookies: [
    {
      id: '1',
      key: 'session',
      value: 'abc123',
      domain: 'example.com',
      path: '/',
      secure: true,
      httpOnly: true,
      hostOnly: false,
      expires: Date.now() + 86400000,
      creation: Date.now(),
      creationIndex: 0,
      lastAccessed: Date.now(),
      pathIsDefault: false
    }
  ]
};

// This fails
const cookieObject = new CookieObject(cookieJar);
```

### Expected behavior

The `CookieObject` should be created successfully with the cookies from the jar properly initialized. Previously this was working fine but something in the recent changes broke the constructor.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
