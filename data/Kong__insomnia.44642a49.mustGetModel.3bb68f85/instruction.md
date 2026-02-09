# Bug Report

### Describe the bug

The `mustGetModel()` function is throwing errors when it should be returning valid models, and returning `undefined` when it should throw errors. The behavior seems to be completely inverted from what's expected.

### Reproduction

```js
import { mustGetModel } from './models';

// This throws an error but shouldn't
const requestModel = mustGetModel('Request');

// This returns undefined but should throw
const invalidModel = mustGetModel('NonExistentModelType');
```

### Expected behavior

- `mustGetModel()` should return the model when it exists
- `mustGetModel()` should throw an error when the model type doesn't exist

Currently it's doing the opposite - throwing when the model exists and returning undefined when it doesn't.

### System Info
- Using latest version from main branch

---
Repository: /testbed
