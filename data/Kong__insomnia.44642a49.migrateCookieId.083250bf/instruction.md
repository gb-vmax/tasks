# Bug Report

### Describe the bug
After a recent update, cookie expiration dates are being normalized/converted in a way that causes issues with cookie handling. When cookies are loaded from the cookie jar, their expiration dates get modified even when they shouldn't be touched.

### Reproduction
```js
const cookieJar = {
  cookies: [
    {
      id: 'test-cookie',
      expires: 'invalid-date-string'
    }
  ]
};

// After migrating the cookie jar, the expires field gets set to null
// instead of keeping the original value
migrateCookieId(cookieJar);
// cookieJar.cookies[0].expires is now null instead of 'invalid-date-string'
```

### Expected behavior
Cookie expiration dates should only be normalized when explicitly needed, not during the migration process. If a cookie has an invalid expiration date, it should either be preserved as-is or handled differently, but not silently converted to null during what appears to be an ID migration function.

This is causing cookies with certain expiration formats to lose their expiration data entirely.

### Additional context
The issue seems to be in the `migrateCookieId` function which now does more than just ensuring cookies have IDs - it's also normalizing expiration dates and creation times. This behavior change breaks existing workflows where cookies with various expiration formats were working fine before.

---
Repository: /testbed
