# Bug Report

### Describe the bug

After a recent update, response body compression is not being set correctly. When loading responses that need compression migration, the `bodyCompression` field remains undefined instead of being set to 'zip'.

### Reproduction

```js
const response = {
  bodyCompression: '__NEEDS_MIGRATION__',
  // ... other response fields
};

const migrated = migrateBodyCompression(response);

// Expected: migrated.bodyCompression === 'zip'
// Actual: migrated.bodyCompression === '__NEEDS_MIGRATION__'
```

### Expected behavior

When a response has `bodyCompression` set to `'__NEEDS_MIGRATION__'`, the migration function should update it to `'zip'`. Currently the value is not being assigned to the document object, so responses that need migration are left in an invalid state.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
