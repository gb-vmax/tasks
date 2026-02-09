# Bug Report

### Describe the bug

I'm experiencing an issue where exported properties from the `unist-util-remove-position` vendor module are not enumerable. When I try to iterate over the exported properties or use methods like `Object.keys()`, the exports don't show up.

### Reproduction

```js
const removePosition = require('./jest/vendor/unist-util-remove-position@5.0.0.js');

// Trying to enumerate exports
console.log(Object.keys(removePosition)); // Returns empty array

// Properties exist but are not enumerable
for (let key in removePosition) {
  console.log(key); // Nothing is logged
}

// Direct access still works
console.log(removePosition.removePosition); // Function exists
```

### Expected behavior

The exported properties should be enumerable so they can be discovered through standard JavaScript enumeration methods like `Object.keys()` or `for...in` loops. This is the standard behavior for ES module exports.

### Additional context

This seems to have broken after a recent change. Previously, iterating over the module exports worked as expected. This is causing issues with tooling that relies on enumerating module exports.

---
Repository: /testbed
