# Bug Report

### Describe the bug

After a recent update, cookie jars are rejecting cookies that have valid empty string paths. Previously, cookies with `path: ''` were accepted and stored correctly, but now they're being filtered out during creation.

### Reproduction

```js
const cookieJar = await create({
  parentId: 'workspace_1',
  cookies: [
    {
      key: 'session',
      value: 'abc123',
      domain: 'example.com',
      path: '',  // Empty path should be valid
      secure: false,
      httpOnly: true
    }
  ]
});

// The cookie is missing from the jar
console.log(cookieJar.cookies.length); // Expected: 1, Actual: 0
```

### Expected behavior

Cookies with empty string paths should be accepted and stored. The path should default to '/' during sanitization, but the cookie itself shouldn't be filtered out. Empty paths are valid in the HTTP cookie specification and should be handled gracefully.

### Additional context

This seems to have started happening recently. Our application relies on importing cookies from various sources, and some of them have empty path values. These cookies are now silently dropped, which breaks cookie synchronization functionality.

---
Repository: /testbed
