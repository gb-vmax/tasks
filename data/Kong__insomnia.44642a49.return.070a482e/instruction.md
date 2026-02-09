# Bug Report

### Describe the bug
After a recent update, calling `getById()` on the request model throws an error. The function appears to be completely missing or undefined, causing the application to crash when trying to retrieve a request by its ID.

### Reproduction
```js
import * as models from './models/request';

// This throws an error - getById is not a function
const request = await models.getById('req_123abc');
```

### Expected behavior
The `getById()` function should return a Promise that resolves to the Request object with the specified ID, or null if not found.

### Additional context
This seems to have broken after some refactoring of the request model. The function was working fine before and is used throughout the codebase to fetch individual requests. Now any code path that tries to retrieve a request by ID fails immediately.

---
Repository: /testbed
