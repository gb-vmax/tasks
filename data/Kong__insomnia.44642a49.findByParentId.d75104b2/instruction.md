# Bug Report

### Describe the bug
When trying to retrieve client certificates by parent ID, the function returns incorrect results. It appears that `findByParentId()` is not actually filtering by the parent ID field, causing it to return the wrong certificates or no certificates at all.

### Reproduction
```js
// Create a workspace with some client certificates
const workspaceId = 'wrk_123';

// Add certificates to the workspace
const cert1 = await clientCertificate.create({ parentId: workspaceId, ... });
const cert2 = await clientCertificate.create({ parentId: workspaceId, ... });

// Try to find certificates by parent ID
const certs = await clientCertificate.findByParentId(workspaceId);

// Expected: Returns [cert1, cert2]
// Actual: Returns empty array or wrong results
```

### Expected behavior
`findByParentId()` should return all client certificates that belong to the specified parent (workspace), but instead it's querying by the wrong field.

### System Info
- Version: Latest from main branch
- OS: macOS

---
Repository: /testbed
