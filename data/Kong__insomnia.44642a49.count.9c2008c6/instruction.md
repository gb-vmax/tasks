# Bug Report

### Describe the bug

After a recent update, the application crashes with a syntax error when trying to count database records. The error appears to be related to the `count` function in the database module.

### Reproduction

```js
import { database } from './common/database';

// This causes the application to fail to start
const count = await database.count('Request', { parentId: 'wrk_123' });
```

### Expected behavior

The `count` function should return the number of matching records without any syntax errors. The application should start normally and database queries should work as expected.

### Additional context

This seems to have broken after some changes to the database layer. The application won't even load now - it fails immediately on startup. Looking at the code, it appears there might be an incomplete refactoring or a syntax issue in the database module.

The error occurs before any actual database operations can be performed, suggesting there's a problem with how the code is structured rather than the logic itself.

---
Repository: /testbed
