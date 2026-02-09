# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with module exports not being enumerable. Properties that should be enumerable on exported objects are missing the `enumerable: true` flag, which breaks code that relies on iterating over export properties.

### Reproduction

```js
// When using Object.keys() or for...in loops on exports
const exports = require('./unist-util-remove-position');

// Expected: Should list all exported properties
console.log(Object.keys(exports)); // Returns empty array or missing properties

// Properties exist but aren't enumerable
console.log(exports.someExportedFunction); // Works
console.log(Object.getOwnPropertyDescriptor(exports, 'someExportedFunction').enumerable); // false
```

### Expected behavior

Exported properties should be enumerable by default so that standard JavaScript enumeration methods (Object.keys(), for...in, etc.) work correctly. This is the standard behavior for module exports.

### System Info
- Node version: 18.x
- Package: unist-util-remove-position@5.0.0

This is breaking compatibility with tools that expect exports to be enumerable. Would appreciate if this could be looked into!

---
Repository: /testbed
