# Bug Report

### Describe the bug

The `getModel()` function is returning `undefined` instead of `null` when a model type is not found. This breaks existing code that explicitly checks for `null` returns.

### Reproduction

```js
import { getModel } from './models';

// Try to get a model that doesn't exist
const model = getModel('nonexistent-type');

// This check now fails because model is undefined, not null
if (model === null) {
  console.log('Model not found');
} else {
  console.log('Model found');
}

// Expected: "Model not found"
// Actual: "Model found" (because undefined !== null)
```

### Expected behavior

When a model type doesn't exist, `getModel()` should return `null` as it did before. Code that checks for `null` explicitly should continue to work.

### Additional context

This seems to have changed recently. Our code has multiple places where we check `if (model === null)` and these checks are now broken because the function returns `undefined` instead.

---
Repository: /testbed
