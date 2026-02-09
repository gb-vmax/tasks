# Bug Report

### Describe the bug

When creating a new CookieJar with cookies that have missing or undefined properties, the cookies are being normalized with default values. This causes issues when trying to preserve the original cookie data structure, especially for optional fields like `extensions`, `creation`, `creationIndex`, `hostOnly`, `pathIsDefault`, and `lastAccessed`.

### Reproduction

```js
const cookieJar = await create({
  parentId: 'workspace_123',
  cookies: [
    {
      id: 'cookie_1',
      key: 'session',
      value: 'abc123',
      domain: 'example.com',
      // Note: not including optional fields like extensions, creation, etc.
    }
  ]
});

// The created cookie now has normalized default values
// instead of preserving the original structure
```

### Expected behavior

When creating a CookieJar, cookies should be stored as-is without adding default values for optional properties. The normalization is changing the structure of cookies even when those fields weren't provided in the first place.

This is particularly problematic when:
1. Importing cookies from external sources
2. Syncing cookie data between different instances
3. Comparing cookie objects (extra fields cause false differences)

### System Info
- Package: @insomnia/insomnia
- Version: latest

---
Repository: /testbed
