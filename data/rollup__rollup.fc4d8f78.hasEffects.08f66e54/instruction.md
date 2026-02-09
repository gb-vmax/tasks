# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where side effects aren't being properly detected in certain cases. When using logical operators (`&&`, `||`, `??`) in my code, the bundler seems to be incorrectly evaluating which branches have side effects, leading to unexpected tree-shaking behavior.

### Reproduction

```js
// Example 1: Side effects in right branch not detected correctly
const result = someCondition && functionWithSideEffects();

// Example 2: Similar issue with OR operator
const value = cached || expensiveComputation();
```

In these cases, when the left operand determines the result of the logical expression, the right side should not be evaluated for side effects. However, it appears that side effects are being checked even when the branch won't be executed.

### Expected behavior

The bundler should correctly identify which branch of a logical expression will be used and only check for side effects in the branch that will actually execute. If the left operand short-circuits the expression, the right side's side effects should not be considered.

### Additional context

This seems to affect dead code elimination - code that should be preserved due to side effects is being removed, or vice versa. The issue appears to be related to how the `hasEffects` method evaluates logical expressions.

---
Repository: /testbed
