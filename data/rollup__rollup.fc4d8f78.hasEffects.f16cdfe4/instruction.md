# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where side effects are not being properly detected in certain cases. When the left side of a logical expression has side effects but is not the used branch, those effects seem to be ignored.

### Reproduction

```js
// Example with || operator
const result = functionWithSideEffects() || someValue;

// Example with && operator  
const result2 = functionWithSideEffects() && someValue;
```

In cases where `functionWithSideEffects()` modifies state or has other side effects, but the logical expression's used branch is determined to be different from the left side, the side effects from the left expression are not being tracked correctly.

### Expected behavior

Side effects from the left side of a logical expression should always be detected and tracked, regardless of which branch is ultimately used. The evaluation of the left operand happens at runtime and can have effects that need to be accounted for.

### Additional context

This seems to affect tree-shaking and dead code elimination, as expressions with side effects might be incorrectly removed or optimized away when they shouldn't be.

---
Repository: /testbed
