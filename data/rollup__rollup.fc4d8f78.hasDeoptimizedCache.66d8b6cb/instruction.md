# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions where the deoptimization caching seems to be inverted. When working with ternary operators in my code, the bundler appears to be caching deoptimization states incorrectly, leading to unexpected behavior in certain edge cases.

### Reproduction

```js
// Example code that triggers the issue
const result = condition ? heavyComputation() : fallback;

// The deoptimization cache appears to store the opposite of what's expected
// causing incorrect optimization decisions
```

This manifests when using conditional expressions with side effects or when the test/consequent/alternate branches have different optimization characteristics. The cache state seems to be backwards from what it should be.

### Expected behavior

The deoptimization cache for conditional expressions should correctly track whether the expression has been deoptimized. When a conditional expression is marked as deoptimized, it should remain deoptimized, and vice versa.

### Additional context

This seems to affect how the bundler handles optimization of ternary operators, particularly in cases where branches have different side effect profiles or when dealing with complex nested conditionals.

---
Repository: /testbed
