# Bug Report

### Describe the bug

I'm encountering an issue with side effect detection in multi-expression scenarios. When checking if expressions have effects on interactions at a specific path, the behavior seems inverted - expressions that should be flagged as having effects are being ignored, and vice versa.

### Reproduction

```js
// Example with comma operator creating multiple expressions
const result = (sideEffect1(), sideEffect2(), finalValue);

// When analyzing this for side effects at a given path,
// the detection appears to be backwards
```

This is affecting tree-shaking and dead code elimination. Code that should be preserved because it has side effects is being removed, while code without side effects is being kept.

### Expected behavior

When any expression in a multi-expression sequence has effects on an interaction at a path, the entire multi-expression should be considered to have effects. Currently it seems like the logic is reversed - if one expression has effects, it returns the opposite of what's expected.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
