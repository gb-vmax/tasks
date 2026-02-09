# Bug Report

### Describe the bug

I'm encountering an issue with yield expressions where the spacing between `yield` and its argument is incorrect in certain cases. When the argument immediately follows the yield keyword without a space, an extra space is being inserted at the wrong position.

### Reproduction

```js
// Input code with yield expression
function* generator() {
  yield value;
}
```

When this gets processed, the spacing calculation seems off. The code appears to be checking if the argument starts at position `start + 6` but then inserting a space at position `start + 5`. Since 'yield' is 5 characters long, this logic doesn't align properly.

### Expected behavior

The space should be correctly inserted between `yield` and its argument when needed, maintaining proper JavaScript syntax. The position calculation should match the actual length of the 'yield' keyword.

### Additional context

This seems related to how the AST node calculates positions for rendering. The mismatch between the position check and where the space gets inserted could lead to malformed output or incorrect code generation.

---
Repository: /testbed
