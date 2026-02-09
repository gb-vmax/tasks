# Bug Report

### Describe the bug

Array expressions are not being properly analyzed for side effects. When working with array literals in the code, the tree-shaking behavior seems incorrect - arrays that should be removed during optimization are being kept, or vice versa.

### Reproduction

```js
// Example code that demonstrates the issue
const arr = [1, 2, 3];
arr.push(4); // This interaction should be detected as having side effects

// Or with more complex cases:
const nested = [[1, 2], [3, 4]];
nested[0].splice(0, 1); // Side effect detection appears broken
```

The bundler is not correctly determining whether operations on array expressions have side effects, which leads to incorrect code elimination or retention during the build process.

### Expected behavior

Array expressions should correctly report whether interactions (like method calls) on them have side effects. This is critical for proper tree-shaking and dead code elimination.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
