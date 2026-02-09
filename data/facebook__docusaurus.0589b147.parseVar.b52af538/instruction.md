# Bug Report

### Describe the bug

I'm encountering an issue with destructuring patterns in variable declarations. When using array or object destructuring without initialization, the parser is incorrectly raising an error about "Complex binding patterns require an initialization value" even when the pattern is just a simple identifier.

### Reproduction

```js
// This should work but throws an error
let x;

// Also affects for-in/for-of loops with simple identifiers
for (let item in array) {
  // ...
}
```

The error message suggests that complex binding patterns need initialization, but this is happening even with simple identifier patterns that don't require initialization.

### Expected behavior

Simple identifier patterns (like `let x;`) should be allowed without initialization. The error about complex binding patterns requiring initialization should only apply to actual complex patterns like `let {a, b}` or `let [x, y]` when they don't have an initializer and aren't in a for-in/for-of context.

### Additional context

This seems to have started happening recently. The parser is being too strict about when to require initialization for variable declarations.

---
Repository: /testbed
