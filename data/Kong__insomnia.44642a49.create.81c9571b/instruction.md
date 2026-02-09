# Bug Report

### Describe the bug
I'm trying to create a new ProtoFile but getting an error that doesn't make sense. When I provide a `parentId` in the creation call, it throws an error saying "New ProtoFile missing `parentId`", even though I'm clearly passing it.

### Reproduction
```js
// This throws an error even though parentId is provided
const protoFile = await create({
  parentId: 'wrk_123',
  name: 'my-proto-file.proto'
});

// Error: New ProtoFile missing `parentId`
```

### Expected behavior
The ProtoFile should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context
This seems to have started happening recently. The validation logic appears to be backwards - it's throwing an error when the parentId EXISTS rather than when it's missing.

---
Repository: /testbed
