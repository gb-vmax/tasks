# Bug Report

### Describe the bug

I'm experiencing an issue with the CookieObject class where it appears to be incomplete or corrupted. When trying to use cookies in my scripts, I'm getting unexpected errors related to cookie handling.

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
      creation: new Date().toISOString(),
      creationIndex: 0,
      lastAccessed: new Date().toISOString(),
      pathIsDefault: false
    }
  ]
};

const cookieObject = new CookieObject(cookieJar);
// Errors occur when trying to work with the cookie object
```

### Expected behavior

The CookieObject should be properly initialized with the provided cookie jar and allow normal cookie operations without throwing errors.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

This seems to have started happening recently. The cookie object construction appears to be broken or incomplete based on the errors I'm seeing.

---
Repository: /testbed
