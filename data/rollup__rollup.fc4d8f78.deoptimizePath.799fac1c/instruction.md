# Bug Report

### Describe the bug

I'm encountering an issue with conditional expressions where the consequent branch seems to be ignored in certain optimization scenarios. When using ternary operators in my code, it appears that only the alternate (false) branch is being processed for deoptimization, even when the condition evaluates to true.

### Reproduction

```js
const result = condition ? consequentValue : alternateValue;

// When condition is true and consequentValue has side effects,
// the side effects are not being properly tracked
```

This seems to affect tree-shaking and dead code elimination. Code that should be kept because it's in the consequent branch is being incorrectly optimized away.

### Expected behavior

Both branches of a conditional expression should be properly analyzed for side effects and dependencies. When the condition is known at build time, only the used branch should be processed. When the condition is unknown, both branches should be considered.

### Additional context

This appears to be a regression - my builds were working correctly in previous versions but now I'm seeing unexpected behavior where code that should execute is being removed from the bundle.

---
Repository: /testbed
