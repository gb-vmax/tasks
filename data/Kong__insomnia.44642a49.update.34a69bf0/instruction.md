# Bug Report

### Describe the bug

When updating workspace metadata using the `update()` function, the patch values are being ignored and overwritten by the original workspace metadata values. This makes it impossible to update any workspace metadata fields.

### Reproduction

```js
const workspaceMeta = {
  _id: 'meta_123',
  parentId: 'wrk_456',
  activeRequestId: 'req_old',
  // ... other fields
};

const patch = {
  activeRequestId: 'req_new'
};

// Try to update the active request
update(workspaceMeta, patch);

// Expected: activeRequestId should be 'req_new'
// Actual: activeRequestId remains 'req_old'
```

### Expected behavior

The patch object should override the corresponding fields in the workspace metadata. After calling `update()` with a patch containing `activeRequestId: 'req_new'`, the workspace metadata should reflect this new value.

### System Info

- Insomnia version: latest
- OS: macOS

This appears to be a regression as updating workspace metadata was working in previous versions.

---
Repository: /testbed
