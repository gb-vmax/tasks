# Bug Report

### Describe the bug

I'm experiencing an issue where pure function calls are incorrectly being marked as having side effects when they're assigned to variables or properties. This causes unnecessary code to be included in the bundle even though it has no actual side effects.

### Reproduction

```js
// Pure function that should be tree-shaken when result is unused
const result = pureFunction();

// Assignment to a variable - this should not be considered as having effects
// if the function is pure and the result is never used
let value;
value = anotherPureFunction();
```

The bundler is not properly tree-shaking these assignments even when:
1. The functions are marked as pure
2. The assigned values are never read or used

### Expected behavior

When a pure function is called and its result is assigned but never used, the entire assignment should be tree-shaken away since it has no side effects. The bundler should recognize that assignments involving pure functions don't have effects.

### Additional context

This seems to affect the dead code elimination optimization. Code that should be removed during tree-shaking is being kept in the final bundle, resulting in larger bundle sizes than necessary.

---
Repository: /testbed
