# Bug Report

### Describe the bug

I'm getting an error when trying to create a new GrpcRequestMeta object with a valid `parentId`. The error message says "New GrpcRequestMeta missing `parentId`" even though I'm clearly providing one.

### Reproduction

```js
const meta = create({
  parentId: 'req_123456789'
});
```

This throws an error:
```
Error: New GrpcRequestMeta missing `parentId`
```

### Expected behavior

The GrpcRequestMeta object should be created successfully when a `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

Currently it seems like the validation logic is backwards - it's throwing an error when parentId EXISTS instead of when it's missing.

---
Repository: /testbed
