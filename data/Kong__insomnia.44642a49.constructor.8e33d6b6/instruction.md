# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with the property traversal system. It seems like the code for handling parent-child relationships in property objects got corrupted or incomplete. When trying to work with nested properties, the application fails to load properly.

### Reproduction

```js
const property = new PropertyBase('test');
// Try to traverse parent properties
property.forEachParent({ withRoot: true }, (parent) => {
  console.log(parent);
  return true;
});
```

The code appears to be incomplete - methods like `forEachParent` and `findInParents` are cut off mid-implementation. There's also a new private method `_enrichAncestorWithDepth` that doesn't seem to be called from anywhere and the original implementation logic is missing.

### Expected behavior

The property traversal methods should work correctly to navigate through parent-child hierarchies. The `forEachParent` method should iterate through all parent properties, and `findInParents` should be able to locate specific properties in the ancestor chain.

### Additional context

This seems to have broken after the latest changes to `packages/insomnia-sdk/src/objects/properties.ts`. The file appears to be in an inconsistent state with incomplete method implementations.

---
Repository: /testbed
