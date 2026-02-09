# Bug Report

### Describe the bug

I'm experiencing an issue with cookie handling where cookies with invalid or expired data are not being filtered out properly. The cookie jar seems to be including cookies that should be excluded based on their expiration date or missing required fields.

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
      expires: Date.now() - 86400000, // expired yesterday
      secure: false,
      httpOnly: true
    },
    {
      id: '2',
      key: '', // missing key
      value: 'test',
      domain: 'example.com',
      path: '/'
    },
    {
      id: '3',
      key: 'valid',
      value: 'data',
      domain: '', // missing domain
      path: '/'
    }
  ]
};

const cookieObject = new CookieObject(cookieJar);
console.log(cookieObject.all()); // Still includes expired and invalid cookies
```

### Expected behavior

The cookie object should automatically filter out:
- Cookies with missing required fields (key, domain)
- Cookies that have already expired
- Invalid cookie data

Only valid, non-expired cookies should be accessible through the cookie object.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
