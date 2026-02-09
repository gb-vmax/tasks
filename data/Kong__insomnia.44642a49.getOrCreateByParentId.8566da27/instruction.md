# Bug Report

### Describe the bug

I'm encountering an issue with gRPC request metadata creation. When calling `getOrCreateByParentId()`, it seems like the function is not properly creating new metadata entries even when none exist for the given parent ID.

### Reproduction

```js
// Try to get or create metadata for a gRPC request
const meta = await getOrCreateByParentId(requestId);

// Expected: Should return a valid metadata object
// Actual: Returns an empty or malformed object
```

The issue appears when:
1. No existing metadata exists for a parent request
2. The function attempts to create new metadata
3. The created metadata is missing required fields or is structured incorrectly

### Expected behavior

When `getOrCreateByParentId()` is called and no metadata exists, it should create a new metadata object with the correct structure including the `parentId` field properly set.

### Additional context

This might be related to how the metadata object is being initialized or validated. The function should handle both cases:
- Returning existing metadata when it's found and valid
- Creating new metadata with proper structure when none exists

---
Repository: /testbed
