# Bug Report

### Describe the bug

The `withDescendants` function appears to have a syntax error or malformed code structure. When trying to use this function, the application fails to load or throws an error related to the database module.

### Reproduction

```js
import { database } from './common/database';

// Attempting to use withDescendants
const doc = { _id: 'some-id', type: 'request' };
const descendants = await database.withDescendants(doc);
```

The code fails to execute and the database module seems to have issues loading properly.

### Expected behavior

The `withDescendants` function should work as before, returning all descendant documents for a given parent document. The function should load without errors and be callable with the standard parameters.

### Additional context

This seems to have started happening recently. The function definition looks corrupted or duplicated in the source code. It appears like there might be two function signatures merged together or something went wrong during a code modification.

---
Repository: /testbed
