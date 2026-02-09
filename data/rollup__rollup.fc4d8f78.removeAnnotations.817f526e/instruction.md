# Bug Report

### Describe the bug

When using sequence expressions with annotations (like `/*#__PURE__*/`), the annotation is not being removed from the correct expression in the sequence. It appears that annotations are being removed from the wrong part of the sequence expression.

### Reproduction

```js
// Given a sequence expression like:
/*#__PURE__*/ foo(), bar(), baz()

// The annotation should be removed from the last expression (baz)
// But it's being removed from the first expression (foo) instead
```

This affects tree-shaking behavior when sequence expressions contain pure annotations, as the annotation is not being properly handled for the expression that actually gets evaluated.

### Expected behavior

For a sequence expression, annotations should be removed from the last expression in the sequence (the one that determines the final value), not the first one.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
