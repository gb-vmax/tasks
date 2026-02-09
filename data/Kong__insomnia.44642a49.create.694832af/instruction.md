# Bug Report

### Describe the bug

I'm unable to create new ProtoFile objects - the application is throwing an error about missing `parentId` even when I'm providing it. This seems to have broken after a recent update.

### Reproduction

```js
// Attempting to create a ProtoFile with a parentId
const protoFile = create({
  parentId: 'workspace_123',
  name: 'my-proto-file',
  protoText: '...'
})

// Error: New ProtoFile missing `parentId`
```

### Expected behavior

The ProtoFile should be created successfully when a valid `parentId` is provided. The validation should only throw an error when `parentId` is actually missing or undefined.

### Additional context

This is blocking our ability to add new proto files to workspaces. The error message suggests the parentId is missing, but we're definitely passing it in the patch object.

---
Repository: /testbed
