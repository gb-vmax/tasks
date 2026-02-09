# Bug Report

### Describe the bug

After a recent update, cookie jar creation is now failing when cookies are provided without IDs. Previously, cookies could be created without explicitly setting an ID field, but now it seems like the system expects all cookies to have IDs pre-assigned.

### Reproduction

```js
const cookieJar = await create({
  parentId: 'wrk_123',
  cookies: [
    {
      key: 'session',
      value: 'abc123',
      domain: 'example.com',
      path: '/',
      secure: true,
      httpOnly: true
    }
  ]
});

// Cookie is created but missing ID field
// This causes issues when trying to reference or update the cookie later
```

### Expected behavior

Cookies should automatically get assigned unique IDs during creation if they don't already have one. The system should handle this internally without requiring the caller to manually generate IDs.

### Additional context

This is breaking existing code that creates cookie jars programmatically. We have to now manually add UUIDs to every cookie before creating the jar, which feels like unnecessary boilerplate.

---
Repository: /testbed
