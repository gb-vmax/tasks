# Bug Report

### Describe the bug

When navigating to versioned documentation routes, the wrong version is being detected as active. Specifically, when accessing a path like `/docs/version-1.0/some-page`, the system incorrectly identifies the latest version as active instead of the specific versioned route.

### Reproduction

```js
// Given multiple doc versions with paths:
// - /docs/* (latest version)
// - /docs/version-1.0/*
// - /docs/version-2.0/*

// Navigate to /docs/version-1.0/getting-started
// Expected: version-1.0 should be detected as active
// Actual: latest version (/docs/*) is detected as active
```

The issue appears when you have nested version paths where the latest version path is a prefix of versioned paths. The matching logic seems to be picking up the first match rather than the most specific one.

### Expected behavior

The active version detection should correctly identify versioned routes even when the latest version uses a catch-all pattern. When I navigate to `/docs/version-1.0/page`, it should recognize `version-1.0` as the active version, not the latest version.

### System Info
- Docusaurus version: latest
- Multiple doc versions configured
- Using default routing configuration

---
Repository: /testbed
