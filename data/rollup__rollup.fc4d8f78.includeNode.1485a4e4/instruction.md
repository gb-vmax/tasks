# Bug Report

### Describe the bug

I'm experiencing an issue with `throw` statements not being included correctly in the bundled output. When I have code that throws errors, the throw statements seem to disappear from the final bundle or appear multiple times in unexpected ways.

### Reproduction

```js
function validateInput(value) {
  if (!value) {
    throw new Error('Value is required');
  }
  return value.trim();
}

export { validateInput };
```

When bundling this code, the `throw` statement either:
- Gets removed from the output entirely, or
- Behaves inconsistently across different builds

### Expected behavior

The `throw` statement should be consistently included in the bundle output when the function is used/imported. Error handling code is critical and should not be optimized away.

### Additional context

This seems to affect the tree-shaking behavior. The throw statements are essential for runtime error handling and should always be preserved when the containing function is included in the bundle.

---
Repository: /testbed
