# Bug Report

### Describe the bug

When updating workspace metadata using the `update()` function, the changes from the `patch` parameter are not being applied correctly. Instead of merging the patch into the existing workspace metadata, it appears that the original workspace metadata values are taking precedence over the patch values.

### Reproduction

```js
const workspaceMeta = {
  _id: 'workspace_123',
  parentId: 'parent_123',
  activeRequestId: 'req_1',
  activeEnvironmentId: 'env_1'
};

const patch = {
  activeRequestId: 'req_2',
  activeEnvironmentId: 'env_2'
};

// Call update with the patch
const result = update(workspaceMeta, patch);

// Expected: activeRequestId should be 'req_2'
// Actual: activeRequestId remains 'req_1'
```

### Expected behavior

The `update()` function should apply the values from the `patch` parameter to the workspace metadata, overwriting any existing values where there are conflicts. The patch should have priority over the original workspace metadata values.

### System Info

- Package: insomnia
- Affected file: `packages/insomnia/src/models/workspace-meta.ts`

---
Repository: /testbed
