# Bug Report

### Describe the bug

I'm experiencing an issue where methods on `PropertyBase` objects appear to be missing or incomplete. When trying to use methods like `meta()`, `parent()`, `forEachParent()`, or `findInParents()`, the code seems to be cut off or not properly defined.

### Reproduction

```js
const property = new PropertyBase('test description');

// Trying to access parent
const parent = property.parent();

// Trying to iterate through parents
property.forEachParent({ withRoot: true }, (obj) => {
  console.log(obj);
  return true;
});

// Trying to find property in parents
const found = property.findInParents('someProperty');
```

### Expected behavior

The `PropertyBase` class methods should be fully implemented and work as expected. Methods like `parent()`, `forEachParent()`, and `findInParents()` should execute without issues and return the appropriate values.

### System Info

- Package: insomnia-sdk
- File: packages/insomnia-sdk/src/objects/properties.ts

The class definition seems incomplete or corrupted. Not sure if this is a merge issue or something else, but the methods are not functioning properly.

---
Repository: /testbed
