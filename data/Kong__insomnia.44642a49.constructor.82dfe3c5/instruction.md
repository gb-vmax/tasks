# Bug Report

### Describe the bug

I'm experiencing issues with parent traversal in the SDK after a recent update. When trying to access parent properties or iterate through parent objects, the application crashes or behaves unexpectedly.

### Reproduction

```js
const property = new PropertyBase('test');
// Set up a parent hierarchy
property._parent = parentProperty;

// Trying to traverse parents causes issues
property.forEachParent({ withRoot: true }, (parent) => {
  console.log(parent);
  return true;
});

// Also fails when trying to find properties in parents
const result = property.findInParents('someProperty');
```

### Expected behavior

Should be able to traverse the parent hierarchy and find properties in ancestor objects without errors. The `forEachParent` and `findInParents` methods should work as they did previously.

### Additional context

This seems to have started happening recently. The parent-related functionality appears to be broken or incomplete. Methods like `forEachParent`, `findInParents`, and `parent()` are not working as expected.

---
Repository: /testbed
