# Bug Report

### Describe the bug

I'm experiencing an issue where certain global functions are being incorrectly marked as having side effects even when called without arguments. This is causing unnecessary conservative behavior in the bundler.

### Reproduction

```js
// This should be considered pure but is being treated as impure
const result = Array.from();

// Expected: The bundler should handle this correctly
// Actual: It's being flagged as having effects when it shouldn't
```

When calling certain array-related globals with no arguments or a single argument, they're being treated as if they have side effects, which impacts tree-shaking and optimization.

### Expected behavior

Functions like `Array.from()` when called with 0 or 1 argument should be recognized as pure operations. Only when called with 2+ arguments where the second argument is not an array expression should they be considered to potentially have effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
