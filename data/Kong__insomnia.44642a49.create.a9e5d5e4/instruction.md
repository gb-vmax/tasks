# Bug Report

### Describe the bug

When trying to create a new ProtoDirectory, I'm getting an error saying "New ProtoDirectory missing `parentId`" even though I'm providing a `parentId` in the patch object. This is blocking me from creating proto directories with proper parent relationships.

### Reproduction

```js
const protoDir = {
  name: 'my-proto-dir',
  parentId: 'wrk_123456'
};

// This throws an error: "New ProtoDirectory missing `parentId`"
const result = await protoDirectory.create(protoDir);
```

### Expected behavior

The ProtoDirectory should be created successfully when a `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context

This seems like a regression - it was working fine before. Now it's impossible to create proto directories that are children of a workspace, which breaks the entire proto file organization feature.

---
Repository: /testbed
