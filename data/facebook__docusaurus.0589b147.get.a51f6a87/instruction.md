# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the rehype-stringify vendor module. When properties are being copied from one object to another, the getter functions are not correctly accessing the source properties, and the enumerable flag logic appears to be inverted.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux'
};

const target = {};

// After copying properties using the affected code
// Accessing target.foo returns undefined instead of 'bar'
// Non-enumerable properties are being marked as enumerable and vice versa
```

### Expected behavior

When copying properties between objects:
1. The getter should return the correct value from the source object (using the current iteration key)
2. Non-enumerable properties should remain non-enumerable in the target object
3. Enumerable properties should remain enumerable in the target object

### System Info
- Node version: Latest
- Package: rehype-stringify@10.0.0

This seems to have broken basic object property copying functionality. The copied properties either return wrong values or have incorrect enumerable settings.

---
Repository: /testbed
