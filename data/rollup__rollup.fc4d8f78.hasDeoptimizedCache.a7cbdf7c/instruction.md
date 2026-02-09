# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions that seems to be causing incorrect optimization behavior. When using logical operators (`&&`, `||`, `??`) in my code, the bundler appears to be making wrong assumptions about which branches can be eliminated, leading to unexpected code being included or excluded from the final bundle.

### Reproduction

```js
// Example code that triggers the issue
const config = {
  debug: false,
  logging: true
};

// This logical expression behaves incorrectly
const shouldLog = config.debug && config.logging;

// Expected: shouldLog should be false
// Actual: The bundler seems to optimize this incorrectly
```

After bundling, the output doesn't match what I expect. It seems like the deoptimization cache is not working correctly, causing the bundler to make incorrect assumptions about the values of logical expressions.

### Expected behavior

Logical expressions should be evaluated correctly during the bundling process. The deoptimization mechanism should properly track when expressions need to be re-evaluated rather than being cached.

### System Info

- Rollup version: latest main branch
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The logical expression optimization is behaving strangely and I suspect it's related to how the cache invalidation is being checked.

---
Repository: /testbed
