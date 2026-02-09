# Bug Report

### Describe the bug

I'm experiencing an issue where object properties are not being properly tracked for deoptimization. When working with complex object structures, the deoptimization flags seem to be inverted - properties that should be marked as having unknown deoptimization are not being flagged correctly, and vice versa.

This is causing unexpected behavior in tree-shaking and dead code elimination, where code that should be kept is being removed, or code that should be removed is being kept in the bundle.

### Reproduction

```js
const obj = {
  foo: {
    bar: someFunction()
  }
};

// Access a property that should trigger deoptimization
obj.foo.bar;

// Expected: The property access should be marked with hasUnknownDeoptimizedProperty = true
// Actual: The flag is being set to false instead
```

When analyzing the AST, objects with unknown property access patterns are being flagged incorrectly. This appears to be affecting the optimization passes.

### Expected behavior

The `hasUnknownDeoptimizedProperty` flag should be set to `true` when an object has properties that cannot be statically analyzed. Currently it seems like the boolean value is being flipped somewhere in the setter logic.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
