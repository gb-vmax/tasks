# Bug Report

### Describe the bug

I'm experiencing an issue where functions with parameters aren't being analyzed correctly for side effects. It seems like the first parameter is being skipped during the side effects check, which causes incorrect tree-shaking behavior.

### Reproduction

```js
function example(a, b, c) {
  console.log(a); // This parameter's side effects are not being checked
  return b + c;
}

// The function call should detect side effects from all parameters
example(someEffectfulExpression(), 1, 2);
```

When the first parameter has side effects (like a function call with side effects), those effects are not being detected properly. This leads to code being incorrectly removed during tree-shaking.

### Expected behavior

All function parameters should be checked for side effects, starting from the first parameter (index 0). The tree-shaking analysis should correctly identify when any parameter has side effects and preserve the necessary code.

### Additional context

This appears to affect functions with multiple parameters where the first parameter contains expressions with side effects. The issue manifests during the build process where code that should be preserved gets incorrectly removed.

---
Repository: /testbed
