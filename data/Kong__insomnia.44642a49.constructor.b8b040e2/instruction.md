# Bug Report

### Describe the bug

I'm experiencing an issue where property traversal methods appear to be incomplete or broken. When trying to use parent-related functionality on property objects, the code seems to cut off mid-execution or doesn't complete properly.

### Reproduction

```js
const property = new PropertyBase('test property');

// Attempting to traverse parents
const result = property.findInParents('someProp', (ancestor) => {
  return ancestor.hasOwnProperty('someProp');
});

// Expected to return ancestor or undefined, but behavior is inconsistent
```

### Steps to reproduce:
1. Create a PropertyBase instance with nested parent structure
2. Try to use `findInParents()` method to locate a property in the parent chain
3. The method doesn't complete as expected

### Expected behavior

The `findInParents` method should traverse the entire parent chain and return the first ancestor that matches the criteria, or undefined if none is found. The logic should complete the full traversal.

### Additional context

This seems to affect the parent traversal functionality in general. Methods like `forEachParent` and `findInParents` that rely on walking up the property hierarchy may not be working correctly.

---
Repository: /testbed
