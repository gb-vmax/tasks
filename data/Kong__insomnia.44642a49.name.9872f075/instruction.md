# Bug Report

### Describe the bug

The `projectSchema` name field is generating names with counters instead of returning the simple string 'name'. This is causing unexpected behavior when creating or syncing projects.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// Expected: 'name'
// Actual: 'name-1', 'name-2', etc.
const result = projectSchema.name();
console.log(result); // Outputs something like 'name-1' instead of 'name'
```

When calling `projectSchema.name()` multiple times, it increments a counter and returns values like `'name-1'`, `'name-2'`, etc. instead of consistently returning `'name'`.

### Expected behavior

The `name` field should return a static string `'name'` each time it's called, similar to how `id` returns `'id'` and `rootDocumentId` returns `'rootDocumentId'`.

### Additional context

This seems to have broken the consistency of the schema - the other fields (`id`, `rootDocumentId`) return static strings, but `name` now has this counter behavior that wasn't there before. Not sure why the counter logic was added here.

---
Repository: /testbed
