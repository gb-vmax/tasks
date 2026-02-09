# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where the first expression in a comma-separated sequence is being ignored during side effect detection. This causes the bundler to incorrectly eliminate code that has important side effects.

### Reproduction

```js
// This code should be preserved because the first expression has side effects
const result = (console.log('important!'), someValue);

// After bundling, the console.log is removed even though it should execute
```

Another example:
```js
// Function with side effects in first position
const x = (globalCounter++, 42);

// The increment to globalCounter gets removed incorrectly
```

### Expected behavior

All expressions in a sequence should be checked for side effects, not just the ones after the first. The first expression in a comma operator sequence executes and may have important side effects that need to be preserved.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as this code was working correctly before. The bundler is now being too aggressive in removing what it thinks is dead code.

---
Repository: /testbed
