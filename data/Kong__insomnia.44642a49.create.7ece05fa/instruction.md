# Bug Report

### Describe the bug

I'm trying to create a new ProtoFile but I'm getting an error saying "New ProtoFile missing `parentId`" even though I'm passing a `parentId` in the patch object.

### Reproduction

```js
const newProtoFile = await models.protoFile.create({
  parentId: 'wrk_123456',
  name: 'my-proto-file.proto',
  protoText: 'syntax = "proto3";'
});
```

This throws an error: `Error: New ProtoFile missing 'parentId'`

### Expected behavior

The ProtoFile should be created successfully when a valid `parentId` is provided. The validation should only throw an error when `parentId` is actually missing or undefined.

### Additional context

This seems to be a regression - it was working fine before. Now every attempt to create a ProtoFile with a parentId fails with this validation error.

---
Repository: /testbed
