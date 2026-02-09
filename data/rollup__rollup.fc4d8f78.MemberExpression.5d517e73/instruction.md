# Bug Report

### Describe the bug

I'm encountering an issue where member expressions with dynamic property keys are not being deoptimized correctly. The deoptimization logic seems to be inverted - it's returning early when it should be processing, and processing when it should return early.

### Reproduction

```js
const obj = {};
const key = 'dynamic';

// Accessing properties with dynamic keys
const value = obj[key];

// The deoptimization cache is not being invalidated properly
// when the property key changes
```

This affects scenarios where:
1. Object properties are accessed using computed/dynamic keys
2. The property key changes between accesses
3. Expressions that depend on these member expressions need to be deoptimized

### Expected behavior

When a member expression's property key differs from the cached dynamic property key, the deoptimization cache should be invalidated and all dependent expressions should be deoptimized. Currently it seems like the logic is backwards - it's skipping deoptimization when it should be running it.

### Additional context

This appears to affect tree-shaking behavior when dealing with namespace imports and member expressions. The condition check seems inverted which causes the deoptimization to trigger at the wrong times.

---
Repository: /testbed
