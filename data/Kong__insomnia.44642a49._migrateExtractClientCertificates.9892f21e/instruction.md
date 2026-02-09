# Bug Report

### Describe the bug

I'm experiencing an issue with workspace certificate migration. After a recent update, client certificates are being processed incorrectly during workspace migration. It seems like the migration logic is running when it shouldn't be, causing certificates that were already migrated to be processed again.

### Reproduction

```js
const workspace = {
  certificates: [
    { cert: 'cert1.pem', key: 'key1.pem' },
    { cert: 'cert2.pem', key: 'key2.pem' }
  ]
  // ... other workspace properties
}

// When loading this workspace, the certificates array 
// gets processed even though it's already in the correct format
```

### Expected behavior

The migration function should skip workspaces where certificates are already in array format. It should only migrate workspaces that have certificates in the old format (non-array).

### Additional context

This appears to affect workspaces that have already been migrated. The certificates array is being treated as if it needs migration when it's already in the correct format.

---
Repository: /testbed
