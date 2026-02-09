# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with logical expressions (`||`, `&&`, `??`) during tree-shaking/dead code elimination. The bundler is keeping the wrong branch of logical expressions, leading to unexpected code in the final bundle.

### Reproduction

```js
// Example 1: OR operator
const value1 = true || someExpression();
// Expected: left branch (true) should be kept
// Actual: right branch (someExpression()) is being kept

// Example 2: AND operator  
const value2 = false && someExpression();
// Expected: left branch (false) should be kept
// Actual: right branch (someExpression()) is being kept

// Example 3: Nullish coalescing
const value3 = null ?? 'default';
// Expected: right branch ('default') should be kept
// Actual: left branch (null) is being kept
```

When bundling code with these logical expressions where the left operand is a known literal value, the wrong branch is being included in the output. This results in unnecessary code bloat and potentially incorrect runtime behavior.

### Expected behavior

The bundler should correctly determine which branch of a logical expression will be executed at runtime based on the literal value of the left operand:
- For `||`: if left is truthy, keep left; otherwise keep right
- For `&&`: if left is falsy, keep left; otherwise keep right  
- For `??`: if left is null/undefined, keep right; otherwise keep left

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
