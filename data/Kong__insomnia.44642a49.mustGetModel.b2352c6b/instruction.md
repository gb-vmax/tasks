# Bug Report

### Describe the bug

The `mustGetModel()` function is not throwing an error when it should. When calling this function with an invalid/non-existent model type, it returns `undefined` instead of throwing an error as expected.

### Reproduction

```js
import { mustGetModel } from './models';

// This should throw an error but returns undefined instead
const model = mustGetModel('NonExistentModelType');
console.log(model); // Output: undefined (should have thrown an error)
```

### Expected behavior

The function should throw an error with the message "The model type {type} must exist but could not be found." when the model doesn't exist. Instead, it's returning the undefined model without throwing.

This breaks any code that relies on `mustGetModel()` to validate model existence, as it will silently fail instead of catching issues early.

### System Info
- Package: @insomnia/insomnia
- Version: latest

---
Repository: /testbed
