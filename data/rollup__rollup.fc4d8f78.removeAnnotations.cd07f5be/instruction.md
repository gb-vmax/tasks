# Bug Report

### Describe the bug

When using sequence expressions (comma operator) with pure annotations, the annotations are being removed from the wrong expressions. It appears that only the first expression in the sequence has its annotations removed, but the subsequent expressions keep their annotations intact.

### Reproduction

```js
// Input code with sequence expression and pure annotations
const result = (/*#__PURE__*/foo(), /*#__PURE__*/bar(), /*#__PURE__*/baz());

// Expected output: all pure annotations should be removed
// Actual output: only the first annotation is removed
```

When bundling code that contains sequence expressions with multiple pure annotations, the first expression's annotation gets removed but the rest remain in the output. This causes inconsistent behavior where some pure annotations are preserved when they shouldn't be.

### Expected behavior

All pure annotations in a sequence expression should be handled consistently - either all should be removed or all should be kept, depending on the context. Currently it seems like only the first one is being processed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
