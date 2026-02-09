# Bug Report

### Describe the bug

I'm encountering an issue with the `in` operator when checking for exports in namespace variables. The operator seems to be returning incorrect boolean values when used with namespace exports.

### Reproduction

```js
import * as namespace from './module';

// Checking if an export exists in the namespace
if ('exportedFunction' in namespace) {
  // This condition evaluates incorrectly
  console.log('Export found');
}
```

When using the `in` operator to check whether a specific export exists in a namespace, the evaluation returns the wrong result. This affects tree-shaking and dead code elimination because the bundler can't properly determine which exports are actually being used.

### Expected behavior

The `in` operator should correctly return `true` when an export exists in the namespace and `false` when it doesn't. This is critical for proper static analysis and optimization of module imports.

### Additional context

This appears to affect cases where we're trying to detect the presence of named exports at compile time. The issue seems related to how literal values are being evaluated for binary expressions involving namespace variables.

---
Repository: /testbed
