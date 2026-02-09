# Bug Report

### Describe the bug

After a recent update, the `getById()` function in the request model is not working. When I try to fetch a request by its ID, the function doesn't return anything and seems to be broken.

### Reproduction

```js
import { getById } from './models/request';

// This no longer works
const request = await getById('req_123abc');
// request is undefined or throws an error
```

### Expected behavior

The `getById()` function should return the request object when given a valid request ID, just like it did before. This is a critical function that's used throughout the app to fetch individual requests.

### Additional context

This seems to have broken after some changes to the request model. The `getByParentId()` function appears to have been modified, but `getById()` is now completely non-functional. This is blocking our ability to view or edit individual requests in the UI.

---
Repository: /testbed
