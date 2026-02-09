# Bug Report

### Describe the bug
After a recent update, the project schema's `id` field is generating IDs in an unexpected format. Instead of returning a simple `'id'` string, it's now returning IDs with counters like `'id-1'`, `'id-2'`, etc.

### Reproduction
```js
import { projectSchema } from './type-schemas';

// First call
const id1 = projectSchema.id();
console.log(id1); // Expected: 'id', Got: 'id-1'

// Second call
const id2 = projectSchema.id();
console.log(id2); // Expected: 'id', Got: 'id-2'
```

### Expected behavior
The `projectSchema.id()` should consistently return the string `'id'` for all calls, matching the behavior of other schema fields like `rootDocumentId` and `name`.

### Additional context
This appears to have broken compatibility with existing code that expects a static string value. The schema now contains unused helper functions (`createIdGenerator`, `projectIdGenerator`, `teamIdGenerator`) and the `id` field has been changed to a stateful generator function instead of a simple string factory.

---
Repository: /testbed
