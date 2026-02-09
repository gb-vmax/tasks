# Bug Report

### Describe the bug

The `removeWhere` function appears to be broken - there's a syntax error that prevents the database module from loading. When trying to use any database operations, the application fails to start or throws an error during initialization.

### Reproduction

```js
import { database } from './common/database';

// Any attempt to use database functions will fail
// because the module itself has a syntax error
await database.removeWhere('request', { parentId: 'some-id' });
```

The issue seems to be in the `removeWhere` function definition where there are duplicate function declarations or malformed syntax.

### Expected behavior

The database module should load correctly and `removeWhere` should execute without syntax errors. The function should properly remove documents matching the query.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is blocking all database operations since the module won't even load properly. Would appreciate a quick fix!

---
Repository: /testbed
