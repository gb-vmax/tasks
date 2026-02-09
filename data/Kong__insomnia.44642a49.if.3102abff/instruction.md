# Bug Report

### Describe the bug

The `withDescendants` function appears to have duplicate code blocks causing a syntax error. After a recent change, the function definition has malformed structure with code appearing both inside and outside the function body, making the database module fail to load.

### Reproduction

```js
import { database } from './common/database';

// Try to use withDescendants
const doc = { _id: 'some-id', type: 'request' };
const descendants = await database.withDescendants(doc);
```

The module fails to import/parse due to the syntax error in the function definition.

### Expected behavior

The `withDescendants` function should be properly defined and callable without syntax errors. The function should:
1. Load without errors
2. Accept a document and optional stopType parameter
3. Return an array of descendant documents

### Additional context

Looking at the code, there seems to be a formatting issue where the function has code both before and after its actual definition, creating invalid JavaScript syntax. This is blocking all database operations that depend on this module.

---
Repository: /testbed
