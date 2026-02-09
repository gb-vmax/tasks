# Bug Report

### Describe the bug

I'm experiencing an issue with cookie management where only the first cookie in a cookie jar gets an ID assigned during migration. When I have multiple cookies without IDs, only the first one receives a UUID, and the rest remain without IDs.

### Reproduction

```js
const cookieJar = {
  cookies: [
    { domain: 'example.com', name: 'cookie1' },
    { domain: 'example.com', name: 'cookie2' },
    { domain: 'example.com', name: 'cookie3' }
  ]
};

// After migration, only cookie1 has an ID
// cookie2 and cookie3 are still missing IDs
```

### Expected behavior

All cookies in the jar that don't have an ID should be assigned a unique UUID. The migration should process every cookie in the array, not just the first one.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
