# Bug Report

### Describe the bug

I'm experiencing an issue with object merging in the remark vendor code. When using functionality that relies on the internal `map` function, properties are being assigned in the wrong direction. This causes source objects to be overwritten with destination properties instead of the expected behavior where destination objects should receive source properties.

### Reproduction

```js
const target = { a: 1, b: 2 };
const source = { b: 3, c: 4 };

// After internal map function is called
// Expected: target becomes { a: 1, b: 3, c: 4 }
// Actual: source becomes { a: 1, b: 2, c: 4 }
```

The issue appears to be in the property assignment logic where the left and right parameters are being used incorrectly.

### Expected behavior

When merging objects, the target (left) object should receive properties from the source (right) object, not the other way around. The original object should be modified with new properties, not have its properties copied to the source.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
