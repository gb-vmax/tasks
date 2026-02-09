# Bug Report

### Describe the bug

I'm experiencing an issue where integer properties on objects are not being properly deoptimized in certain scenarios. It seems like the deoptimization logic is skipping cases where it should be processing integer properties, leading to incorrect behavior during tree-shaking or optimization passes.

### Reproduction

```js
const obj = {
  0: 'value',
  1: 'another',
  regularProp: 'test'
}

// When deoptimizing integer properties
// Expected: all integer properties should be marked as deoptimized
// Actual: some integer properties remain optimized incorrectly
```

The issue appears when an object has both regular properties and integer properties (array-like indices). The deoptimization process seems to be returning early when it shouldn't, causing integer properties to not be properly handled.

### Expected behavior

All integer properties should be consistently deoptimized when `deoptimizeIntegerProperties()` is called, regardless of the object's current tracking state. The method should process integer properties even in cases where the object has lost track but hasn't yet deoptimized integers.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be causing issues with code that relies on proper property access patterns during bundling. Any insights would be appreciated!

---
Repository: /testbed
