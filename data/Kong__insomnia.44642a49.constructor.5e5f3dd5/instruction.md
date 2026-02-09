# Bug Report

### Describe the bug

I'm experiencing an issue where the parent traversal methods in PropertyBase are not working correctly. When trying to navigate up the parent chain or search for properties in parent objects, the methods seem to be broken or incomplete.

### Reproduction

```js
const property = new PropertyBase();
const childProperty = new PropertyBase();
childProperty._parent = property;

// Trying to traverse parents doesn't work as expected
const parents = childProperty.forEachParent({ withRoot: true }, (parent) => {
  console.log(parent);
  return true;
});

// Searching for properties in parent chain also fails
const found = childProperty.findInParents('someProperty');
```

### Expected behavior

The `forEachParent` method should iterate through all parent objects in the chain and execute the callback function for each one. The `findInParents` method should search up the parent chain for a specific property and return the first parent that contains it.

Currently these methods don't seem to be functioning properly - the parent traversal appears to be incomplete or cut off.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
