# Bug Report

### Describe the bug

After a recent update, client certificates with empty or whitespace-only hostnames are being filtered out when retrieving certificates by parent ID. Previously, these certificates were returned in the results, but now they're missing from the list.

### Reproduction

```js
// Create a certificate with an empty host
const cert1 = {
  parentId: 'workspace_1',
  host: '',
  // ... other properties
}

// Create a certificate with only whitespace
const cert2 = {
  parentId: 'workspace_1',
  host: '   ',
  // ... other properties
}

// Create a valid certificate
const cert3 = {
  parentId: 'workspace_1',
  host: 'example.com',
  // ... other properties
}

// Retrieve certificates
const certs = await findByParentId('workspace_1')

// Expected: All 3 certificates returned
// Actual: Only cert3 is returned
console.log(certs.length) // prints 1 instead of 3
```

### Expected behavior

All client certificates associated with a parent ID should be returned, regardless of whether the host field is empty, contains only whitespace, or is valid. The filtering logic seems to have been introduced unintentionally and breaks existing functionality where certificates might be created without hosts initially.

### Additional context

This appears to have started happening recently. Our workflow involves creating certificate entries first and then populating the host field later, so this is blocking our use case.

---
Repository: /testbed
