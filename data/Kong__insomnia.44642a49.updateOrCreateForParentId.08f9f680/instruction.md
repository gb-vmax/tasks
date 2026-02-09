# Bug Report

### Describe the bug

I'm experiencing an issue with the `updateOrCreateForParentId` function where it seems to be passing arguments in the wrong order. When I try to update an API spec for a workspace, the function appears to be using the patch object where it should be using the workspaceId, and vice versa.

### Reproduction

```js
const workspaceId = 'wrk_123456';
const patch = {
  fileName: 'my-api-spec.yaml',
  contents: '...'
};

// This call doesn't work as expected
await updateOrCreateForParentId(workspaceId, patch);
```

The function seems to be treating the patch object as if it were the workspaceId when calling `getOrCreateForParentId`, and then passing the workspaceId to `db.docUpdate` where it expects a spec object.

### Expected behavior

The function should:
1. Use the workspaceId to get or create the spec
2. Update that spec with the provided patch object

Instead, it appears to be mixing up these parameters internally.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
