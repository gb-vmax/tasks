# Bug Report

### Describe the bug

When trying to create a new GrpcRequestMeta without providing a `parentId`, the application no longer throws an error as expected. Instead, it continues execution and fails later with a confusing error message.

### Reproduction

```js
// This should throw an error but doesn't anymore
const meta = grpcRequestMeta.create({
  // parentId is missing
});
```

The code used to properly validate that `parentId` was present before attempting to create the GrpcRequestMeta object. Now it seems to just silently accept the missing field and causes issues downstream.

### Expected behavior

Should throw an error with message: `New GrpcRequestMeta missing 'parentId'` when attempting to create a GrpcRequestMeta without a parentId.

### Additional context

This seems to have broken recently. The validation logic that was checking for the presence of `parentId` appears to no longer be working correctly.

---
Repository: /testbed
