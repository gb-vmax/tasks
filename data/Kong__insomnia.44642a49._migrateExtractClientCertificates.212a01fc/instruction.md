# Bug Report

### Describe the bug

After a recent update, workspace migration is failing when certificates array contains invalid entries. The migration process now skips certificates that don't have proper host or certificate material, but it's also preventing the entire `certificates` property from being cleaned up if any certificate fails validation.

### Reproduction

```js
const workspace = {
  _id: 'wrk_123',
  certificates: [
    {
      host: 'example.com',
      cert: 'valid-cert-data'
    },
    {
      host: '',  // Invalid: empty host
      cert: 'some-cert'
    },
    {
      host: 'another.com',
      // Invalid: no certificate material (no cert, key, or pfx)
    }
  ]
};

// After migration, the certificates property is not removed
// and workspace has a _migrationErrors property attached
```

### Expected behavior

The migration should handle invalid certificates gracefully. Previously, all certificates in the array were migrated and the `certificates` property was always removed from the workspace object after migration, regardless of individual certificate validity.

Now the behavior has changed - if any certificate fails validation (missing host or certificate material), the `certificates` property remains on the workspace object and a `_migrationErrors` property is added.

This is causing issues with workspaces that have legacy/incomplete certificate data, as they never complete the migration process properly.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
