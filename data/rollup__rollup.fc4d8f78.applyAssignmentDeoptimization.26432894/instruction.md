# Bug Report

### Describe the bug

I'm experiencing an issue where member expression assignments are not being properly optimized during tree-shaking. It seems like the deoptimization logic isn't working correctly, causing unnecessary code to be included in the bundle even when it should be removed.

### Reproduction

```js
const obj = {
  prop: undefined
};

// Assignment to member expression
obj.prop = someValue;

// The code related to this assignment should be tree-shaken
// when propertyReadSideEffects is enabled, but it's not being
// removed from the bundle as expected
```

### Expected behavior

When tree-shaking is enabled with `propertyReadSideEffects`, assignments to member expressions should be properly analyzed and deoptimized before the assignment flag is set. This ensures that the tree-shaking pass correctly identifies which code can be safely removed.

### Additional context

The issue appears to be related to how member expression assignments interact with the deoptimization logic. The order of operations seems to matter here - the deoptimization should happen before marking the expression as deoptimized, otherwise the tree-shaking pass might not catch all the necessary optimizations.

This is affecting bundle sizes in production builds where dead code should be eliminated.

---
Repository: /testbed
