# Bug Report

### Describe the bug

When trying to update an API spec using `updateOrCreateForParentId`, the function doesn't update the correct document. Instead of updating the API spec that was just retrieved/created, it appears to be passing the wrong parameter to the update function.

### Reproduction

```js
// Try to update an API spec for a workspace
const workspaceId = 'wrk_123';
const updates = { 
  contents: 'updated spec content',
  contentType: 'yaml'
};

await updateOrCreateForParentId(workspaceId, updates);

// The API spec doesn't get updated
// The function seems to be trying to update something else entirely
```

### Expected behavior

The API spec associated with the workspace should be updated with the provided patch data. The function should:
1. Get or create the API spec for the given workspace ID
2. Update that specific API spec document with the patch

### System Info

- Insomnia version: latest
- Affected module: `models/api-spec.ts`

---
Repository: /testbed
