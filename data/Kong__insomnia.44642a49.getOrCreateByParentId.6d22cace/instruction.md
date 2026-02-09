# Bug Report

### Describe the bug

The `getOrCreateByParentId` function in workspace-meta is not creating a new workspace meta document when one doesn't exist. Instead of creating a new document as expected, the function now returns `undefined`.

### Reproduction

```js
// When calling getOrCreateByParentId with a parentId that doesn't have an existing meta document
const meta = await getOrCreateByParentId('workspace_123');

// Expected: A new workspace meta document to be created and returned
// Actual: undefined is returned
```

### Steps to reproduce
1. Call `getOrCreateByParentId` with a parentId that doesn't have an associated workspace meta
2. The function returns `undefined` instead of creating a new meta document
3. This breaks any code that expects a workspace meta object to always be available

### Expected behavior

The function should create and return a new workspace meta document when one doesn't exist for the given parentId. The "getOrCreate" pattern should guarantee that a valid document is always returned.

### Additional context

This appears to be affecting workspace initialization where new workspaces don't get their meta documents created properly.

---
Repository: /testbed
