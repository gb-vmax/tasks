# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations where some declarators in a multi-variable declaration statement aren't being properly deoptimized. This is causing incorrect optimization behavior in certain scenarios.

### Reproduction

```js
// Example with multiple variable declarators
let a = obj.prop, b = obj.method(), c = getValue();

// When the variables are used later, some of them
// retain incorrect optimization state
console.log(a, b, c);
```

When declaring multiple variables in a single statement, it appears that not all of them are being handled correctly during the deoptimization phase. Specifically, the first declarator seems to be skipped entirely, and the behavior alternates for subsequent declarators.

### Expected behavior

All variable declarators in a declaration statement should be deoptimized consistently, regardless of their position in the declaration list. Each declarator should receive the same deoptimization treatment to ensure correct analysis and optimization.

### Additional context

This seems to affect any variable declaration with multiple declarators, regardless of whether it's `var`, `let`, or `const`. The issue becomes apparent when the declared variables are used in ways that depend on proper deoptimization analysis.

---
Repository: /testbed
