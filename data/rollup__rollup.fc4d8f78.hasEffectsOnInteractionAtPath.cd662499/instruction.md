# Bug Report

### Describe the bug

I'm experiencing an issue where arrow functions with the `@__NO_SIDE_EFFECTS__` annotation are not being treated correctly during tree-shaking. Functions that should be considered side-effect-free are being included in the bundle even when their results are unused.

### Reproduction

```js
// input.js
const fn = /* @__NO_SIDE_EFFECTS__ */ () => {
  return someExpensiveComputation();
};

// This call should be removed during tree-shaking
fn();

// The function is called but result is not used
```

When bundling this code, the function call is not being eliminated even though it's annotated as having no side effects and the return value is unused.

### Expected behavior

Arrow functions annotated with `@__NO_SIDE_EFFECTS__` should be properly recognized as side-effect-free, and calls to these functions should be tree-shaken when their results are not used.

### Additional context

This seems to affect specifically arrow functions with the annotation. Regular function declarations with the same annotation work as expected. The issue appears to be related to how the annotation is being evaluated during the side-effects analysis phase.

---
Repository: /testbed
