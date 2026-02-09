# Bug Report

### Describe the bug

I'm experiencing an issue with the `updateByParentId` function in the workspace-meta model. When I try to update workspace metadata using this function, the updates don't seem to be applied correctly to the workspace. The function appears to complete without errors, but the metadata remains unchanged.

### Reproduction

```js
// Try to update workspace metadata
const parentId = 'wrk_123456';
await updateByParentId(parentId, {
  activeActivity: 'debug',
  sidebarFilter: 'updated-filter'
});

// Check the metadata
const meta = await getByParentId(parentId);
console.log(meta.activeActivity); // Still shows old value
console.log(meta.sidebarFilter); // Still shows old value
```

### Expected behavior

The workspace metadata should be updated with the provided patch values. The `activeActivity` and `sidebarFilter` fields (or any other fields in the patch) should reflect the new values after calling `updateByParentId`.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The function returns successfully but the actual database document doesn't get updated with the new values.

---
Repository: /testbed
