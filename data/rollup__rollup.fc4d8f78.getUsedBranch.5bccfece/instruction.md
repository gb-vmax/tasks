# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions (ternary operators) where the wrong branch is being evaluated. When using a ternary expression with a constant condition, the code seems to be executing the opposite branch than what should be selected.

### Reproduction

```js
const value = true ? 'consequent' : 'alternate';
// Expected: 'consequent'
// Actual: 'alternate'

const value2 = false ? 'consequent' : 'alternate';
// Expected: 'alternate'  
// Actual: 'consequent'
```

This happens when the condition can be statically determined at build time. The branches appear to be swapped - when the condition is truthy, the alternate branch is used, and when it's falsy, the consequent branch is used.

### Expected behavior

The ternary operator should evaluate to the consequent (first) branch when the condition is truthy, and the alternate (second) branch when the condition is falsy.

### Additional context

This seems to affect dead code elimination as well - the wrong branch is being kept in the output while the correct branch is being removed.

---
Repository: /testbed
