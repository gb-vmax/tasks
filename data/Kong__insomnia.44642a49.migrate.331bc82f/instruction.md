# Bug Report

### Describe the bug
After a recent update, client certificates are losing their `_id` field during migration. This causes issues when trying to reference or update existing certificates, as the ID is essential for identifying the certificate in the database.

### Reproduction
```js
const cert = {
  _id: 'cert_123',
  type: 'ClientCertificate',
  host: 'example.com',
  // ... other certificate properties
};

const migrated = migrate(cert);
console.log(migrated._id); // undefined - ID is missing!
```

### Expected behavior
The `_id` field should be preserved during migration. All existing fields in the certificate object should remain intact after calling the `migrate()` function.

### Additional context
This appears to be affecting certificate management functionality, as operations that rely on the certificate ID are failing. The migration function should only add/modify fields that need updating, not remove existing ones.

---
Repository: /testbed
