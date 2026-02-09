# Bug Report

### Describe the bug

I'm experiencing an issue with the `update` function in the workspace-meta model. When I try to update workspace metadata, the updates aren't being applied correctly. It seems like the function is not properly updating the workspace meta object with the provided patch data.

### Reproduction

```js
const workspaceMeta = {
  _id: 'meta_123',
  parentId: 'workspace_456',
  activeRequestId: 'req_1',
  // ... other properties
};

const patch = {
  activeRequestId: 'req_2',
  activeEnvironmentId: 'env_1'
};

// Call update
const result = update(workspaceMeta, patch);

// Expected: result should have activeRequestId = 'req_2' and activeEnvironmentId = 'env_1'
// Actual: The updates are not being applied as expected
```

### Expected behavior

When calling `update(workspaceMeta, patch)`, the function should merge the patch into the workspaceMeta object and return the updated object with all the changes from the patch applied.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
