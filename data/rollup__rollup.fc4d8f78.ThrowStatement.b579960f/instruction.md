# Bug Report

### Describe the bug

I'm experiencing an issue with `throw` statements where whitespace handling appears to be incorrect. When there's no space between `throw` and the argument expression, the output is malformed.

### Reproduction

```js
// Input code
throw new Error('test');

// Expected output
throw new Error('test');

// Actual output - missing space
thrownew Error('test');
```

This happens when the throw statement is formatted without explicit whitespace in the source code. The bundler should automatically insert a space after the `throw` keyword when needed, but it seems to be doing the opposite - adding spaces when they already exist and omitting them when they're needed.

### Expected behavior

The bundler should ensure there's always at least one space between the `throw` keyword and the expression being thrown, regardless of how the source code is formatted.

### Additional context

This appears to affect all throw statements in the codebase. The issue manifests during the rendering/output phase when generating the final bundled code.

---
Repository: /testbed
