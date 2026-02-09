# Bug Report

### Describe the bug

I'm experiencing an issue with how binary expressions are being evaluated for side effects. When using the `+` operator with an empty string on the left side in an expression statement, the code is not being treated as having effects, even though it should trigger implicit type coercion.

### Reproduction

```js
// This should be detected as having effects due to type coercion
'' + someValue;

// The empty string concatenation with + operator should be flagged
const result = (function() {
  '' + obj.toString();
})();
```

### Expected behavior

When the `+` operator is used with an empty string literal on the left side in an expression statement context, it should be recognized as having effects since it triggers implicit type coercion at runtime (calling `toString()` or `valueOf()` on the right operand).

Currently, this pattern is not being detected properly, which could lead to incorrect tree-shaking or optimization decisions.

### Additional context

This seems related to how binary expressions detect side effects from implicit type coercion. The pattern `'' + value` is commonly used to coerce values to strings and can have runtime effects if the value has custom `toString()` or `valueOf()` methods.

---
Repository: /testbed
