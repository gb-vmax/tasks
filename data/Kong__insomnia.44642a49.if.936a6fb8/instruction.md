# Bug Report

### Describe the bug

After a recent update, the `withAncestors` function appears to have duplicate code that's causing issues. The function seems to be defined twice in the same location, which is breaking the database module.

### Reproduction

```js
import { database } from './common/database';

// Try to use withAncestors
const doc = { _id: 'test', parentId: 'parent' };
const ancestors = await database.withAncestors(doc);
```

### Expected behavior

The function should work normally and return the document along with its ancestors without any syntax errors or unexpected behavior.

### Additional context

Looking at the code, it seems like there's a malformed function definition where `withAncestors` is declared twice - once at the beginning and once further down. This is causing the function body to be incomplete and the module likely won't even load properly.

This is blocking our ability to use the database module at all since it won't parse correctly.

---
Repository: /testbed
