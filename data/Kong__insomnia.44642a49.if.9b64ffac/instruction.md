# Bug Report

### Describe the bug

The `withDescendants` function appears to have a syntax error that prevents the application from compiling/running. When trying to use the database module, I'm getting errors related to duplicate function declarations.

### Reproduction

```js
import { database } from './common/database';

// Attempting to call withDescendants
const doc = await database.get('request', 'req_123');
const descendants = await database.withDescendants(doc);
```

The code fails to execute and the module doesn't load properly.

### Expected behavior

The `withDescendants` function should work as before, returning all descendant documents of a given parent document. The function should be callable without any compilation/syntax errors.

### Additional context

This seems to have started happening recently. The database module was working fine before, but now there's an issue with the function definition itself that's preventing normal usage.

---
Repository: /testbed
