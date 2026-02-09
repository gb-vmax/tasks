# Bug Report

### Describe the bug

I'm experiencing an issue when creating a new ProtoDirectory. The function seems to be ignoring all the properties I'm passing in the patch object and only using the `parentId`. This means I can't set any custom properties like `name`, `created`, or other fields when creating a new directory.

### Reproduction

```js
const newDirectory = await protoDirectory.create({
  parentId: 'wrk_123',
  name: 'My Proto Files',
  created: Date.now(),
  modified: Date.now()
});

// Expected: newDirectory should have all the properties I passed
// Actual: Only parentId seems to be used, other properties are missing or default values
```

### Expected behavior

When calling `create()` with a patch object containing multiple properties, all those properties should be applied to the newly created ProtoDirectory. The function should respect the entire patch object, not just extract `parentId` from it.

### Additional context

This seems to have broken recently. Previously I could pass in custom properties and they would be applied correctly to the new directory.

---
Repository: /testbed
