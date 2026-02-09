# Bug Report

### Describe the bug

Optional chaining is not working correctly in call expressions. When using the `?.()` syntax, the optional flag seems to be inverted - expressions that should be treated as optional are being treated as non-optional and vice versa.

### Reproduction

```js
// This should be treated as an optional call but isn't
const result = obj?.method();

// Meanwhile, regular calls are incorrectly flagged as optional
const result2 = obj.method();
```

The issue appears to affect how optional call expressions are detected, causing incorrect behavior during code analysis or transformation.

### Expected behavior

Optional call expressions using `?.()` should be correctly identified as optional, and regular call expressions should be identified as non-optional. The optional flag should accurately reflect the syntax used in the source code.

### Additional context

This seems to have broken recently. The logic for detecting optional calls appears to be returning inverted results.

---
Repository: /testbed
