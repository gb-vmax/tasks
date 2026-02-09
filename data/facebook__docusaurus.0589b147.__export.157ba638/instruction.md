# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with property enumeration on exported objects. Properties that should be enumerable are no longer showing up when iterating over objects or using methods like `Object.keys()`.

### Reproduction

```js
// When exporting properties, they should be enumerable
const exported = {};
__export(exported, { prop1: () => 'value1', prop2: () => 'value2' });

// This returns an empty array instead of ['prop1', 'prop2']
console.log(Object.keys(exported));

// Properties exist but aren't enumerable
console.log(exported.prop1); // 'value1'
console.log(Object.keys(exported)); // []
```

### Expected behavior

Exported properties should be enumerable by default so they can be discovered through standard JavaScript enumeration methods like `Object.keys()`, `for...in` loops, or `Object.entries()`.

### Additional context

This seems to have started happening after the latest changes. The properties are still accessible directly, but they're not showing up in any enumeration operations which breaks code that relies on discovering available properties dynamically.

---
Repository: /testbed
