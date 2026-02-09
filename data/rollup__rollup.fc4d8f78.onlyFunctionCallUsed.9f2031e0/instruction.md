# Bug Report

### Describe the bug

Arrow functions are being incorrectly tree-shaken when used as IIFEs (Immediately Invoked Function Expressions). The bundler is removing arrow functions that should be preserved because they have side effects.

### Reproduction

```js
// This arrow function IIFE gets incorrectly removed during bundling
(() => {
  console.log('This should run');
  globalState.initialized = true;
})();

// Expected: The function should execute and set globalState.initialized
// Actual: The entire IIFE is removed from the bundle
```

Another example:

```js
const result = (() => {
  performSideEffect();
  return computeValue();
})();

// The IIFE is tree-shaken out even though it has side effects
```

### Expected behavior

Arrow function IIFEs should be preserved in the bundle when they contain side effects or are assigned to variables. The tree-shaking logic should recognize these patterns and not remove them.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be a regression - the same code bundled correctly in previous versions.

---
Repository: /testbed
