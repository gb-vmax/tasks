# Bug Report

### Describe the bug

Template literals without expressions are being treated incorrectly during literal value evaluation. When I have a simple template literal like `` `hello` `` (with no interpolations), the bundler is not recognizing it as a static string value.

### Reproduction

```js
// This should be treated as a static literal value
const greeting = `hello world`;

// But it seems to be treated as UnknownValue instead
// This affects tree-shaking and optimization
```

The issue occurs with template literals that contain only a single quasi (no expressions/interpolations). These should be recognized as static string literals for optimization purposes, but they're currently being evaluated as unknown values.

### Expected behavior

Template literals without any expressions should be treated the same as regular string literals. The bundler should be able to:
- Perform dead code elimination based on these values
- Optimize property access on these strings
- Inline them when appropriate

### Additional context

This seems to affect how the AST processes TemplateLiteral nodes. Regular strings work fine, but equivalent template literals (without interpolations) behave differently even though they should produce the same result.

---
Repository: /testbed
