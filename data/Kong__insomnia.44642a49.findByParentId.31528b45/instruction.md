# Bug Report

### Describe the bug

Client certificates are not being loaded correctly when trying to fetch them by workspace ID. The `findByParentId()` function appears to be broken and returns no results even when certificates exist for the given workspace.

### Reproduction

```js
// Create a client certificate for a workspace
const cert = await createClientCertificate({
  parentId: 'wrk_123',
  host: 'example.com',
  // ... other certificate properties
});

// Try to fetch certificates for the workspace
const certs = await findByParentId('wrk_123');

// Expected: Returns array with the certificate
// Actual: Returns empty array
console.log(certs); // []
```

### Expected behavior

The function should return all client certificates associated with the specified parent workspace ID.

### Additional context

This seems to have started happening recently. The certificates are being created successfully (I can see them in the database), but querying by parentId doesn't work anymore.

---
Repository: /testbed
