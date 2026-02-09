# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with `import.meta` properties in my code. When accessing properties on `import.meta`, the bundler is treating them as having side effects when they shouldn't, or vice versa. This is causing issues with tree-shaking and dead code elimination.

### Reproduction

```js
// Case 1: Simple property access
const url = import.meta.url;
console.log(url);

// Case 2: Nested property access
const customProp = import.meta.env.MODE;
```

One of these cases is being incorrectly flagged as having side effects or not having side effects, leading to incorrect bundling behavior. The code either gets removed when it shouldn't be, or stays in the bundle when it should be eliminated.

### Expected behavior

- Direct property access on `import.meta` (like `import.meta.url`) should be treated consistently
- The side effect detection should correctly identify when accessing these properties has or doesn't have side effects
- Tree-shaking should work properly with `import.meta` usage

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if this is related to recent changes in how meta properties are handled.

---
Repository: /testbed
