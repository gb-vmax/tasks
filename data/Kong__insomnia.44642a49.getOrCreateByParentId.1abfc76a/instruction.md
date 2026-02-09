# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC request metadata where the `getOrCreateByParentId` function is not working as expected. When I try to get or create metadata for a gRPC request, it seems to return `undefined` instead of the actual metadata object.

### Reproduction

```js
// Try to get or create metadata for a gRPC request
const meta = await getOrCreateByParentId('some-parent-id');

// meta is undefined even though it should either:
// 1. Return existing metadata if it exists
// 2. Create and return new metadata if it doesn't exist
console.log(meta); // undefined
```

### Expected behavior

The function should:
1. Check if metadata exists for the given parentId
2. If it exists, return the existing metadata
3. If it doesn't exist, create new metadata and return it

Currently it seems like the logic is inverted - when metadata exists it returns undefined, and when it doesn't exist it also returns undefined (since the create call result isn't being returned).

### System Info
- Using latest version from main branch
- This affects gRPC request functionality

---
Repository: /testbed
