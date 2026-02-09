# Bug Report

### Describe the bug

I'm encountering an issue with `yield` expressions in my code. When a `yield` expression is used with an argument that immediately follows the keyword (no space), the generated output is malformed - it appears that a space is being inserted at the wrong position.

### Reproduction

```js
function* myGenerator() {
  yield value;
}
```

When this code is processed, the space between `yield` and the argument is not being handled correctly. The output appears to have spacing issues that break the syntax.

### Expected behavior

The `yield` keyword should be properly separated from its argument with a single space when necessary. The generated code should maintain valid JavaScript syntax.

### Additional context

This seems to affect generator functions where the yield expression has an argument. The issue appears to be related to how the AST node calculates the position for inserting the space separator between the keyword and its argument.

---
Repository: /testbed
