# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions (ternary operators) where the bundler seems to be re-analyzing branches that have already been analyzed, leading to performance degradation and potentially incorrect optimization behavior.

### Reproduction

```js
// Example code that triggers the issue
const value = condition ? heavyComputation() : alternativeValue;

// When this conditional expression is processed multiple times,
// the branch resolution analysis runs repeatedly instead of 
// being cached after the first analysis
```

The problem appears when the same conditional expression is encountered during the bundling process. It seems like the analysis state isn't being tracked correctly, causing redundant work.

### Expected behavior

Once a conditional expression's branches have been analyzed, subsequent checks should recognize that the analysis has already been completed and skip re-analyzing. This should improve build performance and ensure consistent optimization results.

### Additional context

This seems to affect projects with complex conditional logic or deeply nested ternary expressions. Build times have noticeably increased in my project after updating to the latest version.

---
Repository: /testbed
