# Bug Report

### Describe the bug

After a recent update, client certificates are not being returned in the expected order when retrieved for a workspace. The certificates appear to be returned in a random/inconsistent order instead of being sorted alphabetically by host.

### Reproduction

```js
// Create multiple client certificates for a workspace
const cert1 = {
  parentId: 'workspace_123',
  host: 'example.com',
  cert: '...',
  key: '...'
}

const cert2 = {
  parentId: 'workspace_123', 
  host: 'api.example.com',
  cert: '...',
  key: '...'
}

const cert3 = {
  parentId: 'workspace_123',
  host: 'beta.example.com', 
  cert: '...',
  key: '...'
}

// Retrieve certificates
const certificates = await findByParentId('workspace_123')

// Expected order: api.example.com, beta.example.com, example.com
// Actual: Inconsistent ordering
```

### Expected behavior

Client certificates should be returned in alphabetical order sorted by the host field. This makes it easier to find and manage certificates in the UI, especially when dealing with multiple certificates for different domains.

### Additional context

This seems to have changed recently - previously the certificates were appearing in a consistent order in the UI. Now they appear randomly which makes it harder to locate specific certificates.

---
Repository: /testbed
