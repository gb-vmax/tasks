# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression handling. When a response object has a `bodyCompression` value of `'__NEEDS_MIGRATION__'`, it's not being migrated correctly. Instead of removing or properly migrating this special value, it seems to be getting set to `'zip'` for all responses, even those that don't need migration.

### Reproduction

```js
const response = {
  bodyCompression: '__NEEDS_MIGRATION__',
  // ... other response properties
}

// After migration, bodyCompression should be removed
// but instead it's being set to 'zip' for responses that already have a valid value
```

This also affects responses that already have a valid `bodyCompression` value - they're incorrectly being overwritten with `'zip'`.

### Expected behavior

- If `bodyCompression` is set to `'__NEEDS_MIGRATION__'`, it should be removed/deleted from the response object
- If `bodyCompression` already has a valid value (not `'__NEEDS_MIGRATION__'`), it should remain unchanged

### System Info
- Insomnia version: latest
- The issue appears to be in the response model migration logic

---
Repository: /testbed
