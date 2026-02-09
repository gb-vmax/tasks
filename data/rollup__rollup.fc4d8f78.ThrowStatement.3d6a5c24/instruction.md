# Bug Report

### Describe the bug

I'm encountering an issue with `throw` statements where whitespace handling seems incorrect. When there's already a space between `throw` and the expression being thrown, an additional space is being prepended, resulting in double spaces in the output.

### Reproduction

```js
// Input code
throw new Error('test');

// Expected output
throw new Error('test');

// Actual output
throw  new Error('test');  // notice the double space
```

This happens when the throw statement already has proper spacing. It looks like the logic for detecting whether to add a space is inverted - it's adding a space when one already exists instead of when it's missing.

### Expected behavior

The bundler should preserve the original spacing of `throw` statements. If there's already a space between `throw` and the argument, no additional space should be added. A space should only be added when the argument immediately follows `throw` without any whitespace.

### Additional context

This appears to affect all throw statements in the bundled output and makes the code look odd with inconsistent spacing.

---
Repository: /testbed
