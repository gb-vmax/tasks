# Bug Report

### Describe the bug

I'm experiencing an issue with workspace certificate migration. When I have a workspace with client certificates in the old format, the migration process seems to be skipping the actual migration and just deleting the certificates property without creating the new certificate models.

### Reproduction

```js
const workspace = {
  _id: 'wrk_123',
  certificates: {
    cert1: {
      host: 'example.com',
      passphrase: 'test',
      cert: 'cert_data',
      key: 'key_data',
      pfx: null
    }
  }
}

// After migration, certificates are lost
// Expected: certificates should be extracted to separate models
// Actual: certificates property is deleted but no new models created
```

### Steps to reproduce

1. Create a workspace with certificates in the old object format (not array)
2. Trigger the migration process
3. The certificates property gets deleted but the certificates aren't migrated to the new format

### Expected behavior

The migration should:
1. Check if certificates is NOT an array (old format)
2. Extract each certificate and create new clientCertificate models
3. Remove the old certificates property after successful migration

Instead, it appears to be checking if certificates IS an array and returning early, which means workspaces with the old certificate format lose their certificates during migration.

### System Info
- Version: Latest main branch
- Platform: All platforms affected

---
Repository: /testbed
