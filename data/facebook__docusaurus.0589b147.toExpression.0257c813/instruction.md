# Bug Report

### Describe the bug

The `toExpression` function in remark-gfm is not handling RegExp objects correctly. When a RegExp is passed as the `find` parameter, it's being converted to a string and then wrapped in a new RegExp with case-insensitive flag, which breaks the original regex pattern and flags.

### Reproduction

```js
// Original RegExp with specific flags
const pattern = /test/g;

// After toExpression processing, the pattern becomes:
// new RegExp(escapeStringRegexp(pattern), "i")
// which evaluates to something like /\/test\/g/i
// instead of preserving the original /test/g

const result = toExpression(pattern);
// Expected: /test/g
// Actual: /\/test\/g/i (escaped and with wrong flags)
```

### Expected behavior

When a RegExp object is passed to `toExpression`, it should be returned as-is without modification. Only string inputs should be converted to RegExp objects. The function should preserve the original regex flags (like `g` for global matching) instead of replacing them with `i` (case-insensitive).

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
