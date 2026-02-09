# Bug Report

### Describe the bug

I'm experiencing an issue with object property deoptimization that's causing incorrect behavior in my build. It appears that when properties should be marked as deoptimized, they're being treated as optimized instead, and vice versa.

### Reproduction

```js
const obj = {
  prop1: someValue,
  prop2: anotherValue
};

// After certain operations that should trigger deoptimization
// The object properties behave as if they're still optimized
// when they should be deoptimized, leading to incorrect output
```

### Expected behavior

When an object entity has unknown deoptimized properties, the internal flag should correctly reflect this state. Currently it seems like the flag is being set to the opposite of what it should be, causing properties that should be deoptimized to remain optimized and potentially leading to incorrect tree-shaking or code generation.

### System Info
- Rollup version: latest
- Node version: 18.x

This is affecting my production build and causing unexpected behavior with property access patterns. Any help would be appreciated!

---
Repository: /testbed
