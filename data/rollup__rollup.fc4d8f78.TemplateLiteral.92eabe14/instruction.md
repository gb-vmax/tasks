# Bug Report

### Describe the bug

Template literals with no expressions are not being properly evaluated as string literals. When a template literal contains only a single quasi (no interpolations), it should be treated as a static string value, but it's currently returning `UnknownValue` instead.

### Reproduction

```js
// Template literal with no expressions
const str = `hello world`;

// This should be optimized as a static string literal
// but is being treated as an unknown value
```

When the bundler encounters a simple template literal like `` `static text` `` with no `${}` expressions, it should recognize this as equivalent to a plain string literal `"static text"` and optimize accordingly. However, it's currently not detecting this case properly.

### Expected behavior

Template literals without any expressions (single quasi, no interpolations) should be evaluated to their literal string value, just like regular string literals. This allows for proper constant folding and tree-shaking optimizations.

### Additional context

This affects code that uses template literals for static strings, which is common in modern JavaScript. The bundler should be able to statically analyze and optimize these cases.

---
Repository: /testbed
