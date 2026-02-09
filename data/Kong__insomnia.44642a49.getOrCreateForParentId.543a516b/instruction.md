# Bug Report

### Describe the bug

I'm experiencing an issue with API spec retrieval in workspaces. When trying to get or create an API spec for a workspace, the function appears to be searching and creating specs using the wrong field. Instead of properly querying by `parentId`, it seems to be using `_id` directly, which breaks the parent-child relationship.

### Reproduction

```js
// Try to get or create an API spec for a workspace
const workspaceId = 'wrk_123456';
const spec = await getOrCreateForParentId(workspaceId, {
  fileName: 'openapi.yaml',
  contents: '...'
});

// The spec is not found even though one exists with parentId = workspaceId
// Instead, a new spec gets created with _id = workspaceId (wrong!)
```

### Expected behavior

The function should:
1. Query for existing specs using `parentId: workspaceId`
2. If not found, create a new spec with `parentId: workspaceId`
3. Maintain the proper parent-child relationship between workspace and API spec

### Actual behavior

The function appears to be using `_id` instead of `parentId`, which means:
- Existing specs with the correct `parentId` are not found
- New specs are created with the workspace ID as their `_id` instead of as their `parentId`
- This breaks the workspace hierarchy and causes duplicate specs

This is preventing me from properly managing API specs within workspaces. Any workspace that has an existing spec can't retrieve it, and attempting to create one results in incorrect data structure.

---
Repository: /testbed
