# Bug Report

### Describe the bug

I'm experiencing an issue with the `updateOrCreateForParentId` function in the API spec model. When trying to update an API spec for a workspace, the function appears to be passing arguments in the wrong order, which causes unexpected behavior.

### Reproduction

```js
// Attempting to update an API spec for a workspace
await updateOrCreateForParentId(workspaceId, {
  contents: 'openapi: 3.0.0...',
  fileName: 'my-api.yaml'
});
```

When calling this function, instead of updating the spec for the correct workspace with the provided patch data, it seems like the parameters are getting mixed up. The workspace ID is being passed where the patch should be, and vice versa.

### Expected behavior

The function should:
1. Retrieve or create the API spec for the given `workspaceId`
2. Update that spec with the provided `patch` object
3. Return the updated spec

### Current behavior

The function appears to be calling `getOrCreateForParentId` with the patch object instead of the workspaceId, and then trying to update with the workspaceId instead of the patch data. This results in incorrect data being stored or errors when trying to access the spec.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
