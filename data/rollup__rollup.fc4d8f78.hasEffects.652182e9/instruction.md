# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where the first expression in a comma-separated sequence is not being evaluated for side effects. This causes unexpected behavior when the first expression has important side effects that should be preserved.

### Reproduction

```js
// Example 1: First expression has side effects
const result = (console.log('first'), console.log('second'), 42);
// Expected: Both 'first' and 'second' should be logged
// Actual: Only 'second' is logged

// Example 2: Function call with side effects
const value = (updateState(), calculateValue(), getFinalResult());
// The updateState() call is being ignored/removed
```

When bundling code that uses sequence expressions, it appears that the first expression is being incorrectly treated as if it has no side effects and may be getting removed during tree-shaking or optimization.

### Expected behavior

All expressions in a sequence expression should be evaluated for side effects, including the first one. Even though only the last expression's value is used, all expressions should be checked because they may contain important function calls, assignments, or other operations with side effects.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how side effects are being detected in comma expressions. Any help would be appreciated!

---
Repository: /testbed
