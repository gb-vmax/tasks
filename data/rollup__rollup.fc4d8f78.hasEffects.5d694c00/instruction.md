# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where side effects are being detected incorrectly. It seems like the first expression in a sequence is always being treated as having side effects, even when it doesn't actually have any.

### Reproduction

```js
// This sequence expression should only have side effects if the expressions inside have them
const result = (pureExpression, anotherPureExpression);

// Expected: No side effects detected
// Actual: Side effects are always detected
```

For example, when bundling code like:

```js
const x = (1, 2, 3);
```

The bundler is treating this as having side effects when it shouldn't, preventing proper tree-shaking and optimization.

### Expected behavior

A sequence expression should only be considered to have side effects if at least one of its constituent expressions has side effects. Pure expressions like literals or simple variable references shouldn't trigger side effect detection.

### Additional context

This appears to affect dead code elimination and tree-shaking. Code that should be optimized away is being kept in the bundle because the sequence expressions are incorrectly flagged as having side effects.

---
Repository: /testbed
