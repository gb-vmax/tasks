# Bug Report

### Describe the bug

When migrating client certificates from workspace to separate certificate models, the migration process doesn't complete properly. The workspace still retains the old `certificates` array property after migration, and the certificate data isn't being extracted into individual certificate models as expected.

### Reproduction

```js
const workspace = {
  _id: 'wrk_123',
  certificates: [
    {
      host: 'example.com',
      cert: 'cert-data',
      key: 'key-data',
      passphrase: 'secret'
    }
  ]
};

// After migration, workspace.certificates should be removed
// but it remains in the workspace object
```

### Steps to reproduce:
1. Create a workspace with the legacy `certificates` array property
2. Trigger the migration process
3. Check the workspace object - the `certificates` property is still present
4. Check for created certificate models - they may not exist

### Expected behavior

After migration:
- The `certificates` property should be removed from the workspace object
- Individual ClientCertificate models should be created for each certificate in the array
- The workspace should be properly updated in the database

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
