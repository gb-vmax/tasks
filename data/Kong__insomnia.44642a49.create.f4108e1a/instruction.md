# Bug Report

### Describe the bug

I'm getting an error when trying to create a new workspace. The application throws an error saying "New WorkspaceMeta missing parentId" even though I'm providing a valid `parentId` in the workspace creation call.

### Reproduction

```js
// Trying to create a workspace with a parentId
const workspaceMeta = create({
  parentId: 'wrk_123456',
  // ... other properties
});
```

This throws an error:
```
Error: New WorkspaceMeta missing parentId {"parentId":"wrk_123456",...}
```

### Expected behavior

The workspace should be created successfully when a `parentId` is provided. The error message suggests that `parentId` is missing, but it's clearly present in the object being passed.

### Additional context

This seems to have started happening recently. Previously, workspaces were being created without any issues. The error message itself is confusing because it shows the `parentId` is actually present in the JSON output.

---
Repository: /testbed
