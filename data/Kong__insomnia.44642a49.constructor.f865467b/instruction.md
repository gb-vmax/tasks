# Bug Report

### Describe the bug

I'm encountering an issue where the `PropertyBase` class seems to have lost most of its functionality. Methods like `parent()`, `forEachParent()`, `findInParents()`, and `meta()` are no longer available or working as expected.

### Reproduction

```js
const property = new PropertyBase('test description');

// These methods are not working anymore
property.parent(); // undefined or error
property.meta(); // undefined or error
property.forEachParent({ withRoot: true }, (obj) => {
  console.log(obj);
  return true;
}); // undefined or error
```

### Expected behavior

The `PropertyBase` class should provide all the parent traversal methods and meta information handling. These methods were working in previous versions and are likely used by other parts of the SDK that depend on this base class.

### Additional context

This appears to affect any code that relies on:
- Parent-child relationships between properties
- Traversing the property hierarchy
- Finding properties in parent objects
- Meta property handling (properties starting with '_')

The class constructor also seems to have changed, which might affect initialization.

---
Repository: /testbed
