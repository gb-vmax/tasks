# Bug Report

### Describe the bug

I'm experiencing an issue with number literal handling in the AST. When accessing properties directly on number literals (like `42.toString()` or `(123).toFixed(2)`), the code is incorrectly flagged as having side effects, which affects tree-shaking and optimization.

### Reproduction

```js
// This should be recognized as side-effect free
const result = (42).toString();

// This should also be side-effect free
const formatted = (3.14159).toFixed(2);

// Direct property access on number literals
const num = 100;
const str = num.valueOf();
```

The bundler is treating these simple number method calls as having side effects when they shouldn't, preventing proper optimization and dead code elimination.

### Expected behavior

Direct property access and method calls on number literals should be correctly identified as side-effect free operations. These are pure operations that don't modify external state and should be optimized accordingly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
