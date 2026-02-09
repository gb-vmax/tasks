# Bug Report

### Describe the bug

When creating a GrpcRequestMeta with a null parentId, the application throws an error saying "Expected the parent of GrpcRequestMeta to be a GrpcRequest". This prevents creating GrpcRequestMeta objects without a parent, which should be allowed.

### Reproduction

```js
// Attempting to create GrpcRequestMeta with null parent
const meta = {
  parentId: null,
  // ... other properties
}

// This throws: "Expected the parent of GrpcRequestMeta to be a GrpcRequest"
```

### Expected behavior

Creating a GrpcRequestMeta with `parentId: null` should be allowed and not throw an error. The validation should only fail when parentId is a non-null value that doesn't correspond to a valid GrpcRequest ID.

### Additional context

This seems to be a validation logic issue where null parentId values are being incorrectly rejected. The check appears to be inverted - it's throwing an error when it should be passing validation.

---
Repository: /testbed
