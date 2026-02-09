# Bug Report

### Describe the bug

After a recent update, the `PropertyBase` class seems to have lost several critical methods. When trying to use methods like `parent()`, `forEachParent()`, `findInParents()`, and `meta()` on property objects, they are no longer available and cause runtime errors.

### Reproduction

```js
const property = new PropertyBase('test description');

// These methods no longer work
const parentObj = property.parent(); // TypeError: property.parent is not a function
const metaData = property.meta(); // TypeError: property.meta is not a function

// Trying to traverse parent hierarchy also fails
property.forEachParent({}, (parent) => {
  console.log(parent);
  return true;
}); // TypeError: property.forEachParent is not a function
```

### Expected behavior

The `PropertyBase` class should expose the following methods:
- `parent()` - to get the parent property
- `meta()` - to retrieve metadata
- `forEachParent()` - to iterate through parent hierarchy
- `findInParents()` - to search for properties in parent chain

These methods were working in previous versions and are needed for property traversal and metadata access.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
