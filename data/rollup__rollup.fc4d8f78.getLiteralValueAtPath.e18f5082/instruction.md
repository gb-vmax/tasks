# Bug Report

### Describe the bug

I'm experiencing an issue with object property access on prototype chains. When accessing properties on objects, the behavior seems inconsistent - sometimes returning `undefined` when it should return `UnknownValue`, or vice versa.

### Reproduction

```js
const obj = {};
// Accessing a string property on an empty object
const value = obj.someProperty;
// Expected: Should handle this consistently

// Also affects nested property access
const nested = obj.foo.bar;
```

The issue appears to be related to how literal values are resolved at different path depths. Single-level string properties are not being handled the same way as before.

### Expected behavior

Object property lookups should consistently return the appropriate value type based on whether the property exists and what type of key is being accessed (string vs number). String properties at the first level should be treated differently from numeric indices.

### Additional context

This seems to have changed recently and is affecting how object prototypes are analyzed. The logic for determining when to return `undefined` vs `UnknownValue` appears to have been inverted or modified incorrectly.

---
Repository: /testbed
