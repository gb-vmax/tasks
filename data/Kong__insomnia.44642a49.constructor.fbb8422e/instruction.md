# Bug Report

### Describe the bug

When trying to use the CookieObject with a valid cookie jar, I'm getting a runtime error. The application crashes when attempting to access cookies from the cookie jar.

### Reproduction

```js
const cookieJar = {
  name: 'my-jar',
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
      creation: Date.now(),
      creationIndex: 0,
      lastAccessed: Date.now(),
      pathIsDefault: false
    }
  ]
};

// This crashes
const cookieObject = new CookieObject(cookieJar);
```

### Expected behavior

The CookieObject should be created successfully with the provided cookie jar and cookies should be accessible. Instead, it throws an error when the cookieJar parameter is not null.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
