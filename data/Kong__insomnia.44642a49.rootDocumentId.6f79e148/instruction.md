# Bug Report

### Describe the bug

When working with project schemas, the `rootDocumentId` field is being generated with unique values instead of returning a consistent value. This causes issues when comparing or matching projects, as the same project will have different `rootDocumentId` values on subsequent calls.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// First call
const id1 = projectSchema.rootDocumentId();
console.log(id1); // e.g., "doc_abc123_0001_xyz789"

// Second call
const id2 = projectSchema.rootDocumentId();
console.log(id2); // e.g., "doc_abc456_0002_def012"

// These should be the same but they're different
console.log(id1 === id2); // false
```

### Expected behavior

The `rootDocumentId` should return a consistent value (like `'rootDocumentId'`) similar to other schema fields such as `id` and `name`. Schema fields are typically meant to define static property names or identifiers, not generate dynamic values.

### Additional context

This is affecting project synchronization logic where we need to reliably identify and match root documents across different operations. The counter and timestamp-based generation makes it impossible to have stable identifiers.

---
Repository: /testbed
