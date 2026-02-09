# Bug Report

### Describe the bug

I'm experiencing an issue with object literals that have a `__proto__` property. When I define `__proto__` as a regular property (using `init` kind), it's not being handled correctly. The prototype chain seems to be getting messed up.

### Reproduction

```js
const obj = {
  __proto__: null,
  foo: 'bar'
}

// Expected: obj should have null prototype
// Actual: prototype handling is broken
```

When creating an object literal with `__proto__: null`, the prototype should be set to null, but it seems like the code is only checking for getter properties instead of regular property initialization.

### Expected behavior

Object literals with `__proto__` as a regular property (not a getter) should properly set the prototype. When `__proto__` is set to `null`, the object should have a null prototype, not inherit from Object.prototype.

### Additional context

This appears to affect how the prototype chain is constructed for object literals. The issue seems related to how the AST distinguishes between different property kinds (init vs get).

---
Repository: /testbed
