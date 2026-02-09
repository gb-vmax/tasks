# Bug Report

### Describe the bug

When calling methods on `undefined` values in member expressions, the code incorrectly allows the operation to proceed without detecting side effects. This causes the bundler to incorrectly optimize away code that should throw runtime errors.

### Reproduction

```js
const obj = {};
// obj.missing is undefined
obj.missing.someMethod();
```

The bundler is not properly detecting that calling a method on `undefined` will cause a runtime error. This results in incorrect tree-shaking where code that should be preserved (because it throws) gets removed.

### Expected behavior

The bundler should recognize that accessing properties or calling methods on `undefined` values will have side effects (throwing an error at runtime) and should not optimize away such code.

### Additional context

This appears to be related to how member expressions check for side effects when the object is undefined. The issue manifests when trying to call methods or access nested properties on undefined values - the bundler treats these as side-effect-free when they should be flagged as having effects.

---
Repository: /testbed
