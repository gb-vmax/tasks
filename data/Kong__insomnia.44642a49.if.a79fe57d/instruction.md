# Bug Report

### Describe the bug

The `withAncestors` function appears to have a syntax error that breaks the database module. When trying to use any database operations, the application fails to load or crashes.

### Reproduction

```js
import { database } from './common/database';

// Try to use withAncestors
const doc = await database.get('Request', someId);
const ancestors = await database.withAncestors(doc);
```

The code fails to execute and the database module doesn't load properly.

### Expected behavior

The `withAncestors` function should work normally and return an array of ancestor documents based on the parent chain. The function should accept an optional `maxDepth` parameter to limit traversal depth.

### Additional context

This seems to have broken after a recent change to the database module. The function definition looks malformed - there appear to be duplicate function declarations or improper nesting that's causing parsing issues.

---
Repository: /testbed
