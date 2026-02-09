# Bug Report

### Describe the bug

I'm encountering an issue when creating new WorkspaceMeta objects. The function seems to be validating the `parentId` incorrectly - it throws an error when a `parentId` IS provided, but should be throwing an error when it's NOT provided.

### Reproduction

```js
// This throws an error but shouldn't
const meta = create({
  parentId: 'workspace_123',
  // ... other properties
});
// Error: New WorkspaceMeta missing parentId {"parentId":"workspace_123",...}

// This doesn't throw an error but should
const meta2 = create({
  // missing parentId
});
// No error thrown, but parentId is required
```

### Expected behavior

The `create()` function should:
1. Throw an error when `parentId` is NOT provided
2. Successfully create the WorkspaceMeta when `parentId` IS provided

Currently it's doing the opposite - rejecting valid inputs and accepting invalid ones.

### Additional context

This is blocking workspace creation in my workflow. Every attempt to create a workspace meta with a valid parentId fails with the "missing parentId" error, even though the parentId is clearly present in the object.

---
Repository: /testbed
