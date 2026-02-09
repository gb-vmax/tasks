# Bug Report

### Describe the bug

I'm encountering an issue with function purity detection when working with identifier references. It appears that functions are being incorrectly marked as pure when they should be considered impure, or vice versa. This affects tree-shaking and side effect detection during bundling.

### Reproduction

```js
// Example scenario where the issue occurs
const myFunction = externalFunction;

// When calling myFunction, the purity check doesn't work as expected
// The function should be treated as impure if either the variable 
// or the identifier itself is impure, but currently it seems to use OR logic
// instead of AND logic

const result = myFunction();
```

### Expected behavior

When determining if a function call is pure, both the variable's purity AND the identifier's purity should be considered. A function should only be marked as pure if BOTH checks pass, not if either one passes.

Currently it seems like the logic is backwards - if the identifier check says it's pure, that overrides the variable's impurity status.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with dead code elimination where side effects are being incorrectly removed from the bundle.

---
Repository: /testbed
