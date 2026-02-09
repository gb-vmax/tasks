# Bug Report

### Describe the bug

After a recent update, I'm getting a runtime error when trying to call `getById()` on the request model. The function seems to have been accidentally removed or merged incorrectly with another function.

### Reproduction

```js
import * as models from './models/request';

// This throws an error
const request = await models.getById('req_123abc');
```

### Expected behavior

The `getById()` function should retrieve a request by its ID and return a Promise that resolves to the Request object or null if not found.

### Error

```
TypeError: models.getById is not a function
```

It looks like the `getById` function definition got lost somehow. The code was working fine before the latest changes to the request model file.

---
Repository: /testbed
