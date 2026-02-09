# Bug Report

### Describe the bug

The database count function is not working correctly. When trying to count documents in the database, I'm getting unexpected behavior where it seems to be using the wrong code path.

### Reproduction

```js
import { database } from './common/database';

// Try to count documents
const count = await database.count('request', { parentId: 'wrk_123' });
console.log(count); // Returns unexpected result
```

### Expected behavior

The count function should properly query the local database and return the number of matching documents. Instead, it appears to be taking the wrong execution path based on the database state.

### Additional context

This seems to have started happening recently. The count operation either fails or returns incorrect results. It looks like there might be an issue with how the function checks the database state and accesses the collection.

---
Repository: /testbed
