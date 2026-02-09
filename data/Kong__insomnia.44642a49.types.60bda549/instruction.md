# Bug Report

### Describe the bug
The `types()` function is returning `undefined` values instead of the expected model types. It seems like the function is trying to access a property that doesn't exist on the model objects.

### Reproduction
```js
import * as models from './models';

// This returns an array with undefined values
const modelTypes = models.types();
console.log(modelTypes); // [undefined, undefined, ...]
```

### Expected behavior
The `types()` function should return an array of valid model type strings (e.g., `['Request', 'Response', 'Workspace', ...]`), not undefined values.

### Additional context
This appears to have broken recently. The function used to work correctly and return proper type identifiers for all registered models.

---
Repository: /testbed
