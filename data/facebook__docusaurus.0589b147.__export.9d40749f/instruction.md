# Bug Report

### Describe the bug

After a recent update, exported properties from modules are not enumerable anymore, which breaks code that relies on iterating over exported members using `for...in` loops or `Object.keys()`.

### Reproduction

```js
import * as myModule from './some-module';

// This no longer works as expected
for (const key in myModule) {
  console.log(key); // Missing most exports
}

// Also affected
const keys = Object.keys(myModule);
console.log(keys); // Only shows the first export
```

### Expected behavior

All exported properties should be enumerable by default so that iteration and reflection work correctly. Previously, all exports were accessible when iterating over the module namespace object.

### Additional context

This appears to affect the rehype-stringify vendor bundle. The issue manifests when trying to enumerate exports from the module - only the first property is enumerable while all subsequent properties are non-enumerable.

---
Repository: /testbed
