# Bug Report

### Describe the bug

I'm encountering an issue where certain global functions are being incorrectly marked as having side effects during the tree-shaking process. This causes code that should be eliminated as pure to be retained in the bundle.

### Reproduction

```js
// This code should be tree-shaken but isn't
const result = someGlobalFunction(['item1', 'item2']);

// Expected: code is removed if result is unused
// Actual: code is kept in the bundle
```

The problem seems to affect functions that accept array arguments. When passing an array literal as the first argument, the bundler is treating it as impure even though it should be considered side-effect free.

### Expected behavior

Global functions that receive array literals as their first argument should be properly analyzed for side effects. If the function is pure and the result is unused, the call should be tree-shaken from the final bundle.

### Additional context

This appears to be a regression - the same code was being properly optimized in earlier versions. The issue specifically manifests when:
1. A global function is called with an array literal
2. The function call result is not used
3. Tree-shaking is enabled

The bundle size is noticeably larger due to these false positives.

---
Repository: /testbed
