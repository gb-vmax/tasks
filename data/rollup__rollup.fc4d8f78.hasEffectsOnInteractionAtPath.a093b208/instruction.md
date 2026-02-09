# Bug Report

### Describe the bug

I'm experiencing an issue with number literal handling in the tree-shaking process. When accessing properties or methods on number literals, the side effect detection seems to be too aggressive, causing valid code to be incorrectly flagged as having side effects.

### Reproduction

```js
// This code is being incorrectly analyzed for side effects
const x = 42;
const result = x.toString();

// Also affects direct number literals
const str = (123).toFixed(2);
```

The bundler appears to be treating simple property/method access on number literals as having side effects when they shouldn't. This is causing issues with dead code elimination and potentially affecting the final bundle size.

### Expected behavior

Accessing built-in methods and properties on number literals (like `.toString()`, `.toFixed()`, `.valueOf()`, etc.) should be recognized as side-effect-free operations. The tree-shaking analysis should correctly identify these as safe operations that don't produce external side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
