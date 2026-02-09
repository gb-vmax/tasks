# Bug Report

### Describe the bug

After a recent update, the `findInParents` method appears to be completely broken. When trying to traverse up the property hierarchy to find a parent with a specific property, the method doesn't return anything or behaves unexpectedly.

### Reproduction

```js
const property = new PropertyBase();
// Set up a hierarchy with nested parents
property.setParent(parentProperty);

// Try to find a property in the parent chain
const result = property.findInParents('someProperty');

// Expected: should return the parent that has 'someProperty'
// Actual: returns undefined or doesn't work as expected
```

### Expected behavior

The method should traverse up the parent chain and return the first ancestor that contains the specified property. If a customizer function is provided, it should use that to determine which ancestor to return.

### Additional context

This seems to have broken after the latest changes to the properties module. The method signature looks correct but the implementation doesn't seem to be working properly. Not sure if this is a merge conflict issue or something else, but the code structure looks odd.

---
Repository: /testbed
