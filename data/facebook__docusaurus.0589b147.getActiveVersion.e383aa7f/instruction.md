# Bug Report

### Describe the bug

When navigating to versioned documentation paths, the active version detection is not working correctly. It seems like the system always returns the latest version regardless of what version path I'm actually on.

### Reproduction

```js
// Navigate to a specific version like /docs/1.0.0/some-page
// Expected: getActiveVersion() should return version 1.0.0
// Actual: Always returns the latest version instead
```

Steps to reproduce:
1. Set up docs with multiple versions (e.g., latest, 1.0.0, 2.0.0)
2. Navigate to a versioned path like `/docs/1.0.0/introduction`
3. The active version returned is always the latest version, not 1.0.0

### Expected behavior

When I'm on `/docs/1.0.0/some-page`, the `getActiveVersion()` function should return the 1.0.0 version object, not the latest version. The version matching should check all versions and return the one that matches the current pathname.

### Additional context

This breaks version-specific features like the version dropdown showing the wrong active version and version banners not appearing correctly.

---
Repository: /testbed
