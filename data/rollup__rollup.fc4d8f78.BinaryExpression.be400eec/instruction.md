# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions where the `+` operator behavior seems inverted. When the left operand is an empty string in an expression statement, it's not being treated as having effects, but when it's a non-empty string, it is.

### Reproduction

```js
// This should have effects (type coercion) but doesn't
'' + someValue;

// This shouldn't have effects but does
'hello' + someValue;
```

The logic appears to be backwards - empty string concatenation should be flagged as having potential side effects due to implicit type coercion, but non-empty strings are being flagged instead.

### Expected behavior

Binary expressions with the `+` operator should correctly identify when implicit type coercion might cause runtime errors. Specifically:
- `'' + value` should be treated as having effects (potential type coercion issues)
- `'non-empty' + value` should not be treated as having effects

### Additional context

This is affecting tree-shaking and optimization behavior in my builds. The bundler is making incorrect assumptions about which expressions have side effects.

---
Repository: /testbed
