# Bug Report

### Describe the bug

The `upsert` function in the database module appears to have duplicate code that's causing syntax errors. When trying to use the database upsert functionality, the application fails to compile/run.

### Reproduction

```js
import { database } from './common/database';

const doc = {
  _id: 'test-id',
  type: 'request',
  name: 'Test Request',
  modified: Date.now()
};

// This should upsert the document
await database.upsert(doc);
```

### Expected behavior

The upsert operation should work without compilation errors. The function should either insert a new document if it doesn't exist, or update an existing one.

### Additional context

Looking at the code, it seems like there's malformed function definitions - the `upsert` function has nested function declarations and duplicate logic for checking `existingDoc`. The closing brace placement also looks incorrect.

This is blocking our ability to use the database module at all since the file won't compile.

---
Repository: /testbed
