# Bug Report

### Describe the bug

I'm experiencing an issue with the `findInParents` method where it seems to be returning incomplete or corrupted results. The method appears to have been modified recently, but now when I try to use it, I'm getting unexpected behavior - sometimes it returns undefined when it should find a parent, and other times the traversal seems to stop prematurely.

### Reproduction

```js
const childProperty = new PropertyBase();
// Set up parent hierarchy
const parent = new PropertyBase();
const grandparent = new PropertyBase();

childProperty.setParent(parent);
parent.setParent(grandparent);

// Try to find a property in parents
const result = childProperty.findInParents('someProperty');

// Expected: should traverse up the hierarchy and find the property
// Actual: returns undefined or behaves inconsistently
```

### Expected behavior

The `findInParents` method should correctly traverse the parent hierarchy and return the first ancestor that has the specified property. It should work consistently across multiple calls with the same parameters.

### Additional context

This seems to have started happening after a recent update to the properties module. The method worked fine before, but now it's not reliably finding parent properties even when they exist in the hierarchy.

---
Repository: /testbed
