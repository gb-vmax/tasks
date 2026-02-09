# Bug Report

### Describe the bug

When creating a new CookieJar with cookies that have `undefined` values for optional fields like `path`, `secure`, or `httpOnly`, the creation fails with validation errors. These fields should have sensible defaults applied automatically, but instead the validation is rejecting them.

### Reproduction

```js
const cookieJar = await create({
  parentId: 'workspace_123',
  cookies: [
    {
      key: 'session',
      value: 'abc123',
      domain: 'example.com'
      // path, secure, httpOnly not specified
    }
  ]
});
```

This throws an error even though `path`, `secure`, and `httpOnly` are optional fields that should default to `'/'`, `false`, and `false` respectively.

### Expected behavior

The CookieJar should be created successfully with default values applied to any missing optional cookie fields. Cookies without `path` should default to `'/'`, and boolean fields like `secure` and `httpOnly` should default to `false`.

### Additional context

This seems to be happening because the validation is running before defaults are applied. Previously, cookies with missing optional fields were accepted without issues.

---
Repository: /testbed
