# Bug Report

### Describe the bug

I'm able to create ProtoFile objects without providing a `parentId`, which should be a required field. The validation that's supposed to prevent this isn't working correctly.

### Reproduction

```js
// This should throw an error but doesn't
const protoFile = create({
  name: 'test.proto'
  // parentId is missing
});

console.log(protoFile); // Successfully created without parentId
```

### Expected behavior

The `create()` function should throw an error with the message "New ProtoFile missing `parentId`" when `parentId` is not provided in the patch object.

### Additional context

This is causing issues downstream where code expects all ProtoFile objects to have a valid `parentId`. The validation check seems to be inverted - it's allowing creation when it should be blocking it.

---
Repository: /testbed
