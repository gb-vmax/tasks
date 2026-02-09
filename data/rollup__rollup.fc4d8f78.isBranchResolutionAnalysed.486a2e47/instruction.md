# Bug Report

### Describe the bug

I'm encountering an issue with logical expressions where the branch resolution analysis seems to be inverted. When working with code that contains logical operators (`&&`, `||`, `??`), the compiler is behaving as if already-analyzed branches need to be re-analyzed, and vice versa.

### Reproduction

```js
// Example code that triggers the issue
const result = condition1 && condition2 || fallback;

// The logical expression analysis appears to be checking
// the inverse of what it should be checking
```

This causes the compiler to repeatedly analyze the same branches or skip branches that should be analyzed, leading to incorrect optimization behavior.

### Expected behavior

The branch resolution analysis should correctly track which logical expression branches have already been analyzed and avoid redundant analysis, while ensuring all necessary branches are properly evaluated.

### Additional context

This seems to affect any code with complex logical expressions, particularly when they're nested or chained together. The issue appears to be related to how the analysis state is being checked internally.

---
Repository: /testbed
