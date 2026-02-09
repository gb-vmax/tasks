# Bug Report

### Describe the bug
After a recent update, exported properties from modules are no longer enumerable. This is causing issues when trying to iterate over module exports or use methods like `Object.keys()` on exported objects.

### Reproduction
```js
// Module exports
const myModule = require('./some-module');

// This no longer works - returns empty array
console.log(Object.keys(myModule));

// Properties exist but aren't enumerable
console.log('someProperty' in myModule); // true
console.log(Object.keys(myModule).includes('someProperty')); // false
```

### Expected behavior
Exported properties should be enumerable by default so that standard JavaScript iteration methods work correctly. `Object.keys()`, `for...in` loops, and spread operators should be able to access the exported properties.

### Additional context
This appears to have broken after updating the remark-gfm vendor bundle. The exports are still accessible directly by name, but they don't show up in any enumeration operations which is breaking compatibility with existing code that relies on iterating over module exports.

---
Repository: /testbed
