# Bug Report

### Describe the bug

I'm encountering an issue with return statements in the bundler output. When a return statement has an argument that's immediately adjacent to the `return` keyword (no space), the bundler is incorrectly adding a space in the wrong position, breaking the code.

### Reproduction

```js
// Input code
function test() {
  return/* comment */42;
}
```

After bundling, the output becomes malformed. The space handling for return statements seems to be broken when there's already whitespace or a comment between `return` and its argument.

### Expected behavior

The bundler should correctly preserve or add spaces for return statements:
- When `return` is directly followed by its argument with no space, a space should be added
- When there's already whitespace/comments between `return` and the argument, no additional space should be added

The current behavior appears to be doing the opposite - adding spaces when they already exist and potentially not adding them when needed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
