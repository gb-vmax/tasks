# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations where only the second declarator in a multi-variable declaration statement seems to be processed, while the first and any subsequent declarators are being skipped.

### Reproduction

```js
// Multiple variable declarations in a single statement
let a = foo(), b = bar(), c = baz();

// Expected: all three variables (a, b, c) should be properly tracked
// Actual: only 'b' appears to be handled correctly
```

This seems to affect how the compiler tracks side effects and optimizations for variables declared together. The first variable in the declaration list is completely ignored, and if there are more than two variables, only the second one gets processed.

### Expected behavior

All variables in a declaration statement should be processed equally, regardless of their position in the declaration list. Each declarator should have its path deoptimized properly.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be a regression as I didn't see this behavior in earlier versions. Any help would be appreciated!

---
Repository: /testbed
