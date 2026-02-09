# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in the first element of an array are being completely ignored during tree-shaking analysis. It appears that only elements after the first one are being checked for side effects, which causes incorrect code elimination.

### Reproduction

```js
// Example code that demonstrates the issue
const array = [
  sideEffectFunction(),  // This call gets removed incorrectly
  pureFunction(),
  anotherSideEffect()
];
```

When the first element in an array has side effects (like a function call that modifies global state, performs I/O, etc.), it's being treated as if it has no effects and gets removed during the build process. This leads to runtime errors or unexpected behavior because critical code is being eliminated.

### Expected behavior

All elements in the array should be checked for side effects, including the first one. Code with side effects should be preserved regardless of its position in the array.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as it was working correctly in previous versions. Any array where the first element has side effects will be affected by this issue.

---
Repository: /testbed
