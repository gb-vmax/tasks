# Bug Report

### Describe the bug

The `types()` function is returning undefined values instead of the expected model type strings. After some recent changes, calling `types()` results in an array with undefined elements or incorrect nested type properties.

### Reproduction

```js
import * as models from './models';

// Get all model types
const modelTypes = models.types();

console.log(modelTypes);
// Expected: ['Request', 'Response', 'Workspace', ...]
// Actual: [undefined, undefined, ...] or nested type objects
```

### Expected behavior

The `types()` function should return an array of strings representing the type property of each model, not undefined values or nested type objects.

### Additional context

This seems to have started happening recently. The function used to work correctly and return a flat array of type strings like `['Request', 'Response', 'Workspace']` etc. Now it's either filtering out valid types or trying to access a nested `.type.type` property that doesn't exist.

---
Repository: /testbed
