# Bug Report

### Describe the bug

After a recent update, `getById()` is no longer working and causing the application to break. When trying to fetch a request by its ID, I'm getting errors because the function doesn't return anything.

### Reproduction

```js
import { getById } from './models/request';

// Try to get a request by ID
const request = await getById('req_123456');
// This fails - getById doesn't return a promise anymore
```

### Expected behavior

`getById()` should return a Promise that resolves to the Request object (or null if not found), just like it did before. The function should query the database and return the result.

### Additional context

It looks like the function body was accidentally removed or corrupted. The function signature is still there but it doesn't actually do anything now - there's no return statement or database query.

This is blocking our workflow since we can't retrieve individual requests by their ID anymore.

---
Repository: /testbed
