# Bug Report

### Describe the bug

When updating workspace metadata, the changes aren't being persisted correctly. The `update` function seems to be ignoring the patch data and the workspace doesn't get updated as expected.

### Reproduction

```js
const workspaceMeta = {
  _id: 'meta_123',
  parentId: 'wrk_456',
  activeRequestId: 'req_old'
};

// Try to update the active request
await update(workspaceMeta, { activeRequestId: 'req_new' });

// The activeRequestId should be 'req_new' but it remains 'req_old'
```

### Expected behavior

The workspace metadata should be updated with the new values from the patch object. After calling `update`, the returned workspace meta should reflect the changes provided in the patch parameter.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
