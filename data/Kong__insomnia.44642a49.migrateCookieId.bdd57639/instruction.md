# Bug Report

### Describe the bug

After a recent update, cookie jar operations are failing when cookies have expiry dates stored as strings or numbers. The application throws errors when trying to work with cookies that have non-Date expiry values, even though these formats were previously accepted.

### Reproduction

```js
const cookieJar = {
  cookies: [
    {
      id: 'test-cookie',
      key: 'sessionId',
      value: 'abc123',
      expires: '2024-12-31T23:59:59Z'  // String format
    },
    {
      id: 'another-cookie',
      key: 'token',
      value: 'xyz789',
      expires: 1735689599000  // Unix timestamp
    }
  ]
};

// Operations on these cookies now fail
```

### Expected behavior

The cookie jar should handle expiry dates in multiple formats (Date objects, ISO strings, and Unix timestamps) without errors. Previously stored cookies with string or numeric expiry values should continue to work.

### Additional context

This seems to have started after some changes to cookie normalization logic. Cookies that were saved in older versions of the app can no longer be loaded properly.

---
Repository: /testbed
