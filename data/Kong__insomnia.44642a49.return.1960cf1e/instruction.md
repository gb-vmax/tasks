# Bug Report

### Describe the bug

After a recent update, I'm unable to retrieve requests by ID. The `getById` function appears to be broken and is not returning any results.

### Reproduction

```js
import { getById } from './models/request';

// Try to fetch a request by its ID
const request = await getById('req_abc123');

// request is undefined/null even though the ID exists in the database
console.log(request); // null
```

### Expected behavior

The `getById` function should return the request object when a valid ID is provided. This was working fine before but seems to have stopped working after the latest changes.

### Additional context

This is blocking me from loading individual requests in the UI. The function just returns null for every ID I try, even ones that I know exist in the database.

---
Repository: /testbed
