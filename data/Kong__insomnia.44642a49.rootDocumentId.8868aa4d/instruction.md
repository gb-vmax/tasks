# Bug Report

### Describe the bug

After a recent update, the project schema is generating dynamic `rootDocumentId` values instead of returning a static string. This causes issues when working with project synchronization as the `rootDocumentId` changes on every call instead of remaining constant.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// First call
const id1 = projectSchema.rootDocumentId();
console.log(id1); // Returns something like: doc_abc123_0001_xyz789

// Second call
const id2 = projectSchema.rootDocumentId();
console.log(id2); // Returns something like: doc_abc123_0002_def456

// These should be the same but they're different
console.log(id1 === id2); // false (expected: true)
```

### Expected behavior

The `rootDocumentId` should return a consistent value (like the string `'rootDocumentId'`) rather than generating a new unique ID each time it's called. This is breaking project synchronization because the root document ID keeps changing.

### Additional context

This appears to have broken the schema validation logic. The schema is supposed to define the structure/keys of the object, not generate unique identifiers dynamically. Other fields like `id` and `name` correctly return static strings.

---
Repository: /testbed
