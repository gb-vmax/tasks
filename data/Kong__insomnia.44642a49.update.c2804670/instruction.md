# Bug Report

### Describe the bug

The `update` function in workspace-meta is not working correctly. When I try to update workspace metadata, the changes don't seem to be persisted properly. It looks like the function signature or parameter order might have gotten mixed up in a recent change.

### Reproduction

```js
const workspaceMeta = {
  _id: 'meta_123',
  parentId: 'wrk_456',
  activeRequestId: 'req_789',
  // ... other properties
};

const patch = {
  activeRequestId: 'req_999'
};

// Try to update the workspace meta
await update(workspaceMeta, patch);

// The update doesn't apply correctly
```

### Expected behavior

The workspace metadata should be updated with the new `activeRequestId` value. The patch should be merged with the existing workspaceMeta object and persisted to the database.

### Additional context

This seems to have broken recently. Previously, updating workspace metadata worked fine, but now updates either don't persist or get applied incorrectly. The issue appears to be in the `update` function implementation in `workspace-meta.ts`.

---
Repository: /testbed
