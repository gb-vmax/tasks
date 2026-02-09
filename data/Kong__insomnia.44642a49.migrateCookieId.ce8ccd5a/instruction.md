# Bug Report

### Describe the bug

I'm experiencing an issue with cookie management where cookies are getting duplicate IDs assigned. It seems like the migration logic for ensuring cookies have IDs is overwriting existing IDs instead of only adding IDs to cookies that don't have them.

### Reproduction

```js
const cookieJar = {
  cookies: [
    { id: 'existing-id-123', name: 'session', value: 'abc' },
    { name: 'token', value: 'xyz' }
  ]
};

// After update/migration
// Expected: First cookie keeps 'existing-id-123', second gets new ID
// Actual: Both cookies get new IDs assigned
```

### Expected behavior

Cookies that already have an ID should keep their existing ID. Only cookies without an ID should get a new UUID assigned during migration.

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
