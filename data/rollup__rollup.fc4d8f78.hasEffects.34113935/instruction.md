# Bug Report

### Describe the bug

I'm experiencing an issue where `throw` statements are being incorrectly removed from my bundled code during tree-shaking. The bundler seems to be treating throw statements as having no side effects, which causes them to be eliminated even when they should be preserved.

### Reproduction

```js
function validateInput(value) {
  if (!value) {
    throw new Error('Value is required');
  }
  return value.toUpperCase();
}

// When bundling, the throw statement gets removed
// The bundled output doesn't include the error throwing logic
```

After bundling, the validation logic is completely stripped out, which breaks error handling in my application. The throw statement should always be preserved since it has observable side effects.

### Expected behavior

Throw statements should never be tree-shaken away as they have side effects (they interrupt program flow and can be caught by error handlers). The bundled code should preserve all throw statements regardless of whether their result is used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
