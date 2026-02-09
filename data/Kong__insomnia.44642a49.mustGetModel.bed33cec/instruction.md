# Bug Report

### Describe the bug
The `mustGetModel()` function is throwing an error when a valid model type is passed to it, which is the opposite of what it should do. It seems like the function is now throwing errors for models that exist instead of models that don't exist.

### Reproduction
```js
import { mustGetModel } from './models';

// This should work but throws an error
const requestModel = mustGetModel('Request');
// Error: The model type Request must exist but could not be found.

// Even though the model clearly exists
const model = getModel('Request');
console.log(model); // Returns the actual model object
```

### Expected behavior
`mustGetModel()` should only throw an error when the model type doesn't exist. When a valid model type is provided, it should return the model without throwing an error.

### Additional context
This is breaking our application in multiple places where we rely on `mustGetModel()` to retrieve models. The function worked correctly before but now fails for all valid model types.

---
Repository: /testbed
