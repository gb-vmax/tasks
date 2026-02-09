# Bug Report

### Describe the bug

I'm experiencing an issue with property parent traversal after a recent update. When trying to find properties in parent objects, the lookup is not working as expected. The `findInParents` method seems to be incomplete or broken.

### Reproduction

```js
const childProperty = new PropertyBase();
const parentProperty = new PropertyBase();
childProperty._parent = parentProperty;

// This doesn't work anymore
const result = childProperty.findInParents('someProperty');
// Expected to find the property in parent chain, but returns undefined
```

### Expected behavior

The `findInParents` method should traverse the parent chain and locate properties that exist in ancestor objects. It should also support custom filtering via the customizer function.

### Additional context

This appears to have broken after some refactoring. The parent traversal logic seems incomplete - the code just stops mid-implementation. Also noticed that `forEachParent` might be affected too since it relies on similar parent chain traversal.

---
Repository: /testbed
