# Bug Report

### Describe the bug

When using object destructuring with properties that have side effects in their values, the side effects are not being detected properly. This causes the bundler to incorrectly tree-shake code that should be preserved.

### Reproduction

```js
const obj = {
  key: 'test',
  value: sideEffect()  // This side effect is being ignored
}

const { value } = obj;
```

The side effect in the property value should be preserved during bundling, but it's being removed as if it were pure code.

### Expected behavior

Properties with side effects in their values should be detected and the code should not be tree-shaken away. Both key and value side effects need to be considered when determining if a property has effects.

### Additional context

This appears to affect object properties where the value expression has side effects (like function calls, assignments, etc.). The key side effects are being checked but the value side effects seem to be evaluated but not actually used in the final determination.

---
Repository: /testbed
