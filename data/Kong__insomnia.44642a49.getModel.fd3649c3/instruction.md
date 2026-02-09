# Bug Report

### Describe the bug

The `getModel()` function is not finding models when the type parameter is passed with exact casing. It seems like the function is now doing case-insensitive matching and trimming whitespace, which causes issues when looking up models by their exact type string.

### Reproduction

```js
import { getModel } from './models';

// Assuming we have a model with type 'Request'
const model = getModel('Request');

// model is now undefined instead of the expected model object
console.log(model); // undefined
```

Previously this would return the model object, but now it returns `undefined`. The issue appears when you pass the exact type string that matches the model's type property.

### Expected behavior

`getModel('Request')` should return the Request model object (or `null` if not found), not `undefined`. The function should match model types exactly as they are defined without any transformations.

### System Info
- Package: insomnia
- Version: latest

---
Repository: /testbed
