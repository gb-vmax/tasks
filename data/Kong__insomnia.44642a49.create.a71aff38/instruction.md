# Bug Report

### Describe the bug

I'm encountering an issue when creating a new GrpcRequestMeta object. The function throws an error about missing `parentId` even when `parentId` is provided in the patch object.

### Reproduction

```js
const meta = create({
  parentId: 'some-grpc-request-id',
  // other properties...
});
```

This throws: `New GrpcRequestMeta missing 'parentId'`

### Expected behavior

The GrpcRequestMeta should be created successfully when a valid `parentId` is provided. The validation should only fail if `parentId` is actually missing or invalid.

### Additional context

This seems to have started happening recently. The error is thrown even though I'm definitely passing a `parentId` in the patch object. The validation check appears to be running before it should be able to access the `parentId` value.

---
Repository: /testbed
