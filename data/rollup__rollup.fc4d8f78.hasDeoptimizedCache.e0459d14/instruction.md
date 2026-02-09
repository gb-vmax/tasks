# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions (&&, ||, ??) where they're not being properly optimized during the build process. It seems like the deoptimization cache is behaving incorrectly, causing expressions that should be optimized to remain unoptimized.

### Reproduction

```js
// Example code that triggers the issue
const result = someCondition && expensiveFunction();

// Or with nullish coalescing
const value = maybeNull ?? defaultValue;
```

When bundling code with logical expressions like these, the output is not as optimized as expected. The expressions appear to be deoptimized even when they should remain optimized based on static analysis.

### Expected behavior

Logical expressions should be properly optimized when possible. The deoptimization cache should correctly track which expressions have been deoptimized, so that optimization decisions are made accurately.

### Additional context

This seems to affect all types of logical expressions (AND, OR, nullish coalescing). The build output is larger than it should be and may contain unnecessary code branches.

---
Repository: /testbed
