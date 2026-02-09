# Bug Report

### Describe the bug

After a recent update, response migration is failing silently. When there's an error during the `migrateBodyCompression` process, the migration doesn't return the migrated document correctly. This causes responses to not be properly migrated even when the compression migration succeeds.

### Reproduction

```js
// Create a response document that needs migration
const response = {
  _id: 'res_123',
  bodyCompression: 'old_format',
  // ... other response properties
};

// Attempt to migrate
const migrated = migrate(response);

// Expected: migrated response with updated bodyCompression
// Actual: migrated is undefined
```

### Expected behavior

The `migrate()` function should return the migrated response document after successfully running `migrateBodyCompression()`. Currently it returns `undefined` when migration completes without errors.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
