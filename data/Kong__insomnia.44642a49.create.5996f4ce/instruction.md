# Bug Report

### Describe the bug

When creating a new CookieJar, the creation fails or produces incorrect results. The CookieJar is not being properly associated with its parent workspace.

### Reproduction

```js
const cookieJar = await models.cookieJar.create({
  parentId: 'wrk_123',
  cookies: []
});

// The cookieJar is created but not properly linked to the workspace
// or the creation fails entirely
```

### Expected behavior

The CookieJar should be created successfully and properly associated with the specified `parentId` (workspace). The created CookieJar should be retrievable and functional for the parent workspace.

### System Info

- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
