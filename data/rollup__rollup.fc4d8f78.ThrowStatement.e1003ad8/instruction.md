# Bug Report

### Describe the bug

I've noticed that `throw` statements are being rendered incorrectly when there's whitespace between `throw` and the argument expression. The bundler is adding an extra space even when one already exists.

### Reproduction

```js
// Input code
throw    new Error('test');

// Expected output
throw    new Error('test');

// Actual output
throw     new Error('test');  // extra space added
```

The issue seems to happen when there's already whitespace present between the `throw` keyword and the expression being thrown. The bundler is prepending an additional space unnecessarily.

### Expected behavior

The bundler should preserve the existing whitespace or only add a space when there isn't one already present. Currently it's adding a space regardless of whether whitespace already exists between `throw` and its argument.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
