# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new CookieJar without a `parentId`. The behavior seems to be inverted - it throws an error when `parentId` is provided and succeeds when it's missing.

### Reproduction

```js
// This should fail but doesn't
const cookieJar = await create({
  name: 'My Cookie Jar'
  // no parentId
});

// This should succeed but throws an error instead
const cookieJar2 = await create({
  name: 'My Cookie Jar',
  parentId: 'workspace_123'
});
```

### Expected behavior

- Creating a CookieJar **without** a `parentId` should throw an error with message: `New CookieJar missing 'parentId'`
- Creating a CookieJar **with** a `parentId` should succeed and return the created document

### Current behavior

The validation logic appears to be backwards - it accepts CookieJars without `parentId` and rejects those with `parentId`.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
