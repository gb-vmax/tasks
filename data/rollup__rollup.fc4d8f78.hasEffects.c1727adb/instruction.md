# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where side effects are not being properly detected in certain cases. It seems like when using logical operators (`&&`, `||`, `??`), the bundler is incorrectly determining whether the right-hand side expression has effects.

### Reproduction

```js
// Case 1: Logical AND with side effects on right side
const result = someCondition && functionWithSideEffects();

// Case 2: Logical OR with side effects on right side  
const value = existingValue || initializeWithSideEffects();

// Case 3: Nullish coalescing with side effects
const config = userConfig ?? setDefaultConfig();
```

In these scenarios, the right-hand side functions have side effects (like modifying global state, making API calls, etc.), but they're being treated as if they don't have effects when the left side determines the branch is used.

### Expected behavior

The bundler should correctly identify that the right-hand side of logical expressions can have side effects and should be evaluated accordingly. When the left branch is used/taken, it should still check if the right side has effects that need to be preserved.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with tree-shaking where important side effects are being removed from the bundle.

---
Repository: /testbed
