# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression handling. After updating, responses that previously had `zip` compression are being incorrectly migrated to `__NEEDS_MIGRATION__` status, which breaks the ability to view compressed response bodies.

### Reproduction

```js
const response = {
  bodyCompression: 'zip',
  // ... other response properties
}

// After migration runs, bodyCompression is now '__NEEDS_MIGRATION__'
// instead of staying as 'zip'
```

### Expected behavior

Responses with `bodyCompression: 'zip'` should maintain their compression type and not be marked as needing migration. The migration logic should only affect responses that actually have `__NEEDS_MIGRATION__` as their compression value.

### System Info
- Insomnia version: latest
- Platform: Cross-platform issue

---
Repository: /testbed
