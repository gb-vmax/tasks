# Bug Report

### Describe the bug

I'm experiencing an issue with return statements in functions where side effects in the return expression are not being properly tracked. When a return statement contains an expression with side effects (like function calls), the bundler seems to be incorrectly handling the control flow analysis.

### Reproduction

```js
function example() {
  return sideEffectFunction();
}
```

In this case, when the function contains a return statement with an expression that has side effects, the side effects should be detected before the control flow is marked as broken. However, it appears that the control flow is being marked as broken too early, which affects how the bundler analyzes whether the code has effects.

This is particularly problematic when:
1. The return statement contains a function call with side effects
2. The bundler needs to determine if the code should be tree-shaken
3. The return statement is inside a context where return/yield is being tracked

### Expected behavior

The bundler should properly detect side effects in return statement expressions before marking the control flow as broken. Side effect analysis should happen in the correct order to ensure accurate tree-shaking decisions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
