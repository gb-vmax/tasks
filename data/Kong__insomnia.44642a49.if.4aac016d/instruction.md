# Bug Report

### Describe the bug

The `withAncestors` function appears to have duplicate function declarations in the database module. When calling this function, it seems like the code is malformed and may cause syntax errors or unexpected behavior.

### Reproduction

```js
import { database } from './common/database';

const doc = {
  _id: 'doc123',
  parentId: 'parent456',
  type: 'request'
};

// Attempting to get ancestors
const ancestors = await database.withAncestors(doc, ['workspace', 'project']);
```

### Expected behavior

The function should return an array of ancestor documents without any syntax errors or duplicate declarations. The code should compile and execute properly.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
