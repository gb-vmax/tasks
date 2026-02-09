# Bug Report

### Describe the bug

I'm experiencing an issue with the cookie handling in the Insomnia SDK. After a recent update, cookies are not being loaded properly from the cookie jar. When I try to access cookies through the SDK, I'm getting an empty list even though the cookie jar contains valid cookies.

### Reproduction

```js
const insomniaCookieJar = {
  name: 'my-jar',
  cookies: [
    {
      id: '1',
      key: 'session_id',
      value: 'abc123',
      domain: '.example.com',
      path: '/',
      secure: true,
      httpOnly: true,
      hostOnly: false,
      creation: '2024-01-01T00:00:00.000Z',
      creationIndex: 0,
      lastAccessed: '2024-01-01T00:00:00.000Z',
      pathIsDefault: false
    }
  ]
};

const cookieObject = new CookieObject(insomniaCookieJar);
// Expected: cookieObject should contain the cookie
// Actual: cookieObject appears to be empty or incomplete
```

### Expected behavior

The `CookieObject` constructor should properly initialize with all valid cookies from the provided cookie jar. The cookies should be accessible and properly formatted.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

This seems to have started happening recently. The cookie jar definitely contains the cookies, but they're not being processed correctly when creating the CookieObject instance.

---
Repository: /testbed
