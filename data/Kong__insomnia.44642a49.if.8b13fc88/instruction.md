# Bug Report

### Describe the bug

The `withAncestors` function in the database module appears to have a syntax error that's preventing the application from running. There's a duplicate function declaration that's breaking the code structure.

### Reproduction

When trying to use the database module after a recent update:

```js
import { database } from './common/database';

// Attempting to call withAncestors
const doc = await database.get('Request', someId);
const ancestors = await database.withAncestors(doc);
```

The code fails to execute and the module can't be imported properly.

### Expected behavior

The `withAncestors` function should work normally and return an array of ancestor documents as it did before.

### Additional context

This seems to have started happening after a recent change to the database module. The function declaration looks malformed in the source code - there appears to be a duplicate function signature that's causing parsing issues.

---
Repository: /testbed
