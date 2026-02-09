# Bug Report

### Describe the bug

When creating a new CookieJar with cookies that have missing or invalid fields, the application crashes with an error about missing required fields. This happens even when the cookies have default values that should be applied automatically.

### Reproduction

```js
const cookieJar = await create({
  parentId: 'wrk_123',
  cookies: [
    {
      key: 'session',
      value: 'abc123',
      domain: 'example.com'
      // Missing optional fields like path, secure, httpOnly, etc.
    }
  ]
});
```

The above code throws an error even though fields like `path`, `secure`, and `httpOnly` should have default values applied.

Also having issues when cookies have `expires` as a string:

```js
const cookieJar = await create({
  parentId: 'wrk_123',
  cookies: [
    {
      key: 'token',
      value: 'xyz',
      domain: 'api.example.com',
      expires: '2024-12-31T23:59:59Z'  // String date causes problems
    }
  ]
});
```

### Expected behavior

- Cookies should be created successfully with default values for missing optional fields
- String dates in `expires` field should be handled gracefully
- The cookie jar creation should not fail when optional fields are omitted

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
