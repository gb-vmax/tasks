# Bug Report

### Describe the bug

I'm encountering an issue where ternary conditional expressions seem to be evaluating to the wrong branch. When I have a simple conditional like `condition ? valueIfTrue : valueIfFalse`, the output appears to be inverted - I'm getting the false value when the condition is true, and vice versa.

### Reproduction

```js
// Simple example
const result = true ? 'correct' : 'wrong';
// Expected: 'correct'
// Actual: 'wrong'

// Another case
const value = someCondition ? consequentBranch : alternateBranch;
// When someCondition is truthy, I'm getting alternateBranch instead of consequentBranch
```

This is affecting my build output where conditional expressions are being optimized/tree-shaken. The bundler seems to be keeping the wrong branch of the ternary operator.

### Expected behavior

When a ternary expression evaluates to true, the consequent (first) branch should be used. When it evaluates to false, the alternate (second) branch should be used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
