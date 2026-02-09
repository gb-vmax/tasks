# Bug Report

### Describe the bug

I'm experiencing an issue with the `findInParents` method where it seems to stop working correctly after a recent update. The method is supposed to traverse the parent chain to find a property, but it's not returning the expected results anymore.

### Reproduction

```js
const child = new PropertyBase();
const parent = new PropertyBase();
child.setParent(parent);

// Try to find a property in the parent chain
const result = child.findInParents('someProperty', (ancestor) => {
  return ancestor.meta().hasOwnProperty('someProperty');
});

// Result is undefined even when the property exists in parent
console.log(result); // undefined
```

### Expected behavior

The method should traverse up the parent chain and return the first ancestor that contains the specified property. When a customizer function is provided, it should be called with the ancestor and return the ancestor when the customizer returns true.

### Additional context

This seems to have broken recently. The method just returns undefined now even when the property clearly exists in the parent chain. Not sure if this is related to the cloning logic or something else.

---
Repository: /testbed
