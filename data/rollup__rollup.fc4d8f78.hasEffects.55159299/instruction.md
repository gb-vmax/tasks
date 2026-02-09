# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where side effects are not being detected correctly. It seems like expressions with side effects are being incorrectly marked as having no effects, which causes the bundler to remove code that should be kept.

### Reproduction

```js
// This code should be kept because it has side effects
const result = (console.log('first'), console.log('second'), 42);

// After bundling, the console.log statements are being removed
// even though they have side effects
```

Another case:

```js
// Multiple expressions with side effects
let x = 0;
const value = (x++, x++, x);

// The increments are being treated as if they have no effects
// and the code gets incorrectly optimized away
```

### Expected behavior

Sequence expressions should correctly identify when any of their sub-expressions have side effects. Code with side effects should not be removed during tree-shaking or optimization.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to have started happening recently. The bundler is becoming too aggressive in removing what it thinks is dead code.

---
Repository: /testbed
