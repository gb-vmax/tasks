# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new GrpcRequestMeta object. The creation fails even when a valid `parentId` is provided, which seems backwards.

### Reproduction

```js
// This should work but throws an error
const meta = create({
  parentId: 'valid-grpc-request-id',
  // other properties...
});

// Error: New GrpcRequestMeta missing `parentId`
```

### Expected behavior

When calling `create()` with a valid `parentId`, it should successfully create the GrpcRequestMeta object. The error should only be thrown when `parentId` is actually missing or undefined.

Currently it seems like the validation logic is inverted - it throws an error when parentId EXISTS rather than when it's missing.

### System Info
- Using latest version from main branch

---
Repository: /testbed
