# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where side effects from the left-hand side are not being properly detected. When a logical expression has a left operand with side effects, the bundler seems to incorrectly evaluate whether the entire expression has effects.

### Reproduction

```js
// Example code that demonstrates the issue
const result = (console.log('left'), false) || doSomething();

// The console.log on the left side should be considered as having effects,
// but it appears to be ignored in certain cases
```

The problem occurs when:
1. The left side of a logical expression (`||`, `&&`, `??`) has side effects
2. The expression is evaluated for tree-shaking purposes
3. The left side's effects are not properly accounted for

### Expected behavior

Logical expressions should always check if the left operand has side effects, regardless of which branch will be used. Even if the left side evaluates to a certain value, any side effects it produces (like function calls, assignments, etc.) should still be detected and preserved during bundling.

### Additional context

This seems to affect dead code elimination - code that should be kept due to side effects is being incorrectly removed. The issue appears to be in how the effect detection logic handles the branching behavior of logical operators.

---
Repository: /testbed
