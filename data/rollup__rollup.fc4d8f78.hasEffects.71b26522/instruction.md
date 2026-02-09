# Bug Report

### Describe the bug

When using conditional expressions (ternary operators) in my code, side effects are not being properly detected during tree-shaking. Functions with side effects are being incorrectly removed from the bundle even though they should be preserved.

### Reproduction

```js
// This function has side effects and should be included
function logMessage() {
  console.log('This has side effects');
  return true;
}

// Using a ternary with a test condition that has side effects
const result = logMessage() ? 'yes' : 'no';

// After bundling, the logMessage() call gets removed even though
// it has side effects (console.log)
```

Another case:

```js
const value = someCondition
  ? functionWithSideEffects()  // This gets incorrectly removed
  : anotherFunction();
```

### Expected behavior

Functions with side effects in conditional expressions should be preserved in the output bundle. The tree-shaking process should recognize that these functions need to be executed and not remove them.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started recently. The bundler is being too aggressive with removing code that it thinks is unused but actually has important side effects.

---
Repository: /testbed
