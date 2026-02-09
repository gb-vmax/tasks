# Bug Report

### Describe the bug

When calling `getOrCreateByParentId()`, the function is not returning the correct workspace metadata. If an existing document is found, it creates a new empty document instead of returning the existing one. If no document exists, it returns `undefined` instead of creating a new one with the proper `parentId`.

### Reproduction

```js
// Scenario 1: Existing workspace meta
const existingMeta = await getOrCreateByParentId('workspace_123');
// Returns a new empty document instead of the existing one
// Expected: Should return the existing workspace meta for 'workspace_123'

// Scenario 2: Non-existent workspace meta  
const newMeta = await getOrCreateByParentId('workspace_456');
// Returns undefined
// Expected: Should create and return a new workspace meta with parentId 'workspace_456'
```

### Expected behavior

The function should:
1. Return the existing workspace metadata if found
2. Create and return a new workspace metadata with the correct `parentId` if not found

### Additional context

This appears to have broken workspace initialization logic where metadata is expected to be properly associated with parent workspaces.

---
Repository: /testbed
