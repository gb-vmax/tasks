# Bug Report

### Describe the bug

I'm experiencing an issue with multi-expression sequences where side effects are not being properly detected. When I have a sequence of expressions (comma operator), the side effect analysis seems to be returning incorrect results.

### Reproduction

```js
// Example with sequence expression
const result = (sideEffect1(), sideEffect2(), pureExpression());

// The bundler should detect that this sequence has side effects
// from sideEffect1() and sideEffect2(), but it's treating the
// entire sequence incorrectly
```

When bundling code that contains comma-separated expressions, the tree-shaking behavior is not working as expected. Expressions that should be preserved because they have side effects are being incorrectly analyzed.

### Expected behavior

The bundler should correctly identify when any expression in a sequence has side effects and preserve the entire sequence accordingly. Each expression in the comma operator should be checked for side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect dead code elimination and tree-shaking optimization passes.

---
Repository: /testbed
