# Bug Report

### Describe the bug

The `mustGetModel()` function is returning incorrect values when a model type exists. Instead of returning the model object itself, it's returning something unexpected, which breaks any code that depends on getting the actual model.

### Reproduction

```js
import { mustGetModel } from './models';

// Try to get a valid model type
const model = mustGetModel('request');

// Expected: model should be the actual model object
// Actual: model is not the correct object and causes errors when trying to use it
console.log(model); // This doesn't return what we expect
```

### Expected behavior

When calling `mustGetModel()` with a valid model type, it should return the actual model object so it can be used for database operations. The function should only throw an error when the model type doesn't exist.

### Additional context

This seems to affect any code path that uses `mustGetModel()` to retrieve models. The function appears to have logic issues that prevent it from working correctly even when valid model types are provided.

---
Repository: /testbed
