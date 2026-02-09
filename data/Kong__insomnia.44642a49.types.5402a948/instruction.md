# Bug Report

### Describe the bug

The `types()` function is returning incorrect values. Instead of getting model types as expected, I'm getting `undefined` values in the array.

### Reproduction

```js
import { types } from './models';

const modelTypes = types();
console.log(modelTypes);
// Expected: ['request', 'workspace', 'environment', ...]
// Actual: [undefined, undefined, undefined, ...]
```

### Expected behavior

The `types()` function should return an array of model type strings (e.g., `['request', 'workspace', 'environment']`), not an array of undefined values.

### Additional context

This seems to have broken recently. The function is supposed to extract the `type` property from each model, but something is going wrong with the mapping.

---
Repository: /testbed
