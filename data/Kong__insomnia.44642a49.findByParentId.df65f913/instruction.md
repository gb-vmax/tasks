# Bug Report

### Describe the bug
Client certificates are not being loaded correctly when querying by parent ID. The `findByParentId` function appears to be returning empty results even when valid certificates exist for a given workspace.

### Reproduction
```js
// Create a client certificate with a parent workspace ID
const cert = await clientCertificate.create({
  parentId: 'wrk_123',
  host: 'example.com',
  // ... other cert properties
});

// Try to retrieve certificates for this workspace
const certs = await clientCertificate.findByParentId('wrk_123');

// Expected: Should return the certificate created above
// Actual: Returns empty array or no results
console.log(certs); // []
```

### Expected behavior
The function should return all client certificates associated with the given parent workspace ID. This is breaking certificate selection in the UI when trying to use client certs for requests within a workspace.

### Additional context
This seems to have started happening recently. The certificates are being created successfully (they show up in the database), but the query to retrieve them by parentId isn't working as expected.

---
Repository: /testbed
