# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions where the deoptimization logic seems to be applied at the wrong time. When using optional chaining on method calls (e.g., `obj?.method()`), the behavior is inconsistent compared to regular call expressions.

### Reproduction

```js
// Optional chaining with method call
const result = obj?.someMethod();

// The deoptimization appears to happen differently
// depending on whether the callee is null/undefined
```

The problem seems to occur specifically when:
1. Using optional chaining (`?.`) on a call expression
2. The callee evaluates to null or undefined
3. There are side effects or arguments involved

### Expected behavior

The deoptimization logic should be applied consistently regardless of whether the optional chain is skipped or not. Currently, it seems like the timing of when deoptimizations are applied has changed, which could lead to incorrect optimization decisions or missed side effects.

### Additional context

This appears to affect how the AST handles call expressions with optional chaining, particularly around member expressions. The interaction setup and effect tracking might not be working as intended in edge cases.

---
Repository: /testbed
