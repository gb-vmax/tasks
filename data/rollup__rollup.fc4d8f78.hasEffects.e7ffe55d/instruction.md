# Bug Report

### Describe the bug

Conditional expressions are not being properly tree-shaken when they have side effects. Code that should be removed during the optimization phase is being kept in the bundle, resulting in larger output sizes and potentially executing code that should have been eliminated.

### Reproduction

```js
// Example code that demonstrates the issue
const result = someCondition 
  ? doSomethingWithSideEffects() 
  : doSomethingElseWithSideEffects();

// Expected: Only the used branch should be evaluated for side effects
// Actual: The wrong branch is being checked for side effects
```

When the bundler analyzes conditional expressions to determine if they can be optimized away, it's not correctly identifying which branch will actually be executed. This causes incorrect tree-shaking behavior where code that should be removed is kept, or vice versa.

### Expected behavior

The bundler should correctly analyze conditional expressions and only preserve the branch that will actually be used at runtime. Dead code in the unused branch should be eliminated if it has no side effects.

### Additional context

This appears to affect the static analysis phase where the bundler determines whether expressions have effects that need to be preserved. The logic for checking which branch of a ternary operator has side effects seems to be inverted or not returning the correct result.

---
Repository: /testbed
