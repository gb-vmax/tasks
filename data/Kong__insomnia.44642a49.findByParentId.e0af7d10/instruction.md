# Bug Report

### Describe the bug

When trying to retrieve client certificates by parent ID, the function returns incorrect results. Instead of getting certificates that belong to a specific parent, I'm getting certificates that DON'T belong to that parent. Additionally, even when there are multiple certificates for a parent, only one certificate is being returned.

### Reproduction

```js
// Assuming we have multiple client certificates with the same parentId
const parentId = 'workspace_123';

// Create multiple certificates for the same parent
await createCertificate({ parentId: 'workspace_123', ... });
await createCertificate({ parentId: 'workspace_123', ... });
await createCertificate({ parentId: 'workspace_456', ... });

// Try to find certificates for workspace_123
const certs = await findByParentId('workspace_123');

// Expected: 2 certificates from workspace_123
// Actual: 1 certificate from workspace_456 (wrong parent!)
console.log(certs); // Returns certificate from the WRONG parent
```

### Expected behavior

`findByParentId()` should return ALL client certificates that match the given parentId, not certificates from other parents. If I have 3 certificates under the same workspace, all 3 should be returned.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like a regression - it was working fine before. Not sure what changed but this is blocking certificate management for workspaces with multiple certs.

---
Repository: /testbed
