# Bug Report

### Describe the bug

I'm experiencing incorrect behavior when working with objects that have numeric keys. It seems like the deoptimization logic for integer properties is not working as expected, causing unexpected results in the generated output.

### Reproduction

```js
const obj = {
  0: 'first',
  1: 'second',
  2: 'third'
};

// Accessing properties by numeric index
console.log(obj[0]); // Should work correctly
console.log(obj[1]); // Should work correctly

// Modifying numeric properties
obj[3] = 'fourth';
```

When bundling code that manipulates objects with integer keys, the optimization/deoptimization behavior seems inverted - properties that should be tracked as "unknown" are being treated as known, and vice versa.

### Expected behavior

Objects with integer keys should be properly tracked and deoptimized when necessary. The bundler should correctly identify when integer properties need special handling.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be related to how the AST handles object entities with numeric properties. The behavior changed recently and is causing issues with code that relies on dynamic property access patterns.

---
Repository: /testbed
