# Bug Report

### Describe the bug

I'm encountering an issue with `for...in` loops where side effects aren't being tracked correctly. It seems like the order of evaluation has changed, which is causing some expressions in the loop to be incorrectly optimized away or included when they shouldn't be.

### Reproduction

```js
for (const key in obj) {
  // Side effects in the iterable expression or loop variable assignment
  // are not being detected properly
}
```

When the `for...in` statement has side effects in either:
1. The right-hand side (the object being iterated)
2. The left-hand side (the loop variable assignment)

The bundler doesn't seem to handle them in the correct order anymore. This affects tree-shaking and can result in code being incorrectly removed or retained.

### Expected behavior

Side effects should be evaluated in the proper order:
1. First check the right-hand side (the iterable)
2. Then check the left-hand side (the assignment target)

This ensures that expressions with side effects are properly preserved during the bundling process.

### Additional context

This appears to affect how the AST node determines whether the statement has effects and how it includes child nodes during traversal. The evaluation order matters for correctness.

---
Repository: /testbed
