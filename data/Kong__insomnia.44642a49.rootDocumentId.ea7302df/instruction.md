# Bug Report

### Describe the bug

I'm experiencing an issue with project synchronization where the `rootDocumentId` is being generated with random values instead of using a consistent identifier. This is causing problems when trying to sync or compare projects, as the same project gets different root document IDs on each operation.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// Create a project schema
const project1 = {
  id: projectSchema.id(),
  rootDocumentId: projectSchema.rootDocumentId(),
  name: projectSchema.name()
};

const project2 = {
  id: projectSchema.id(),
  rootDocumentId: projectSchema.rootDocumentId(),
  name: projectSchema.name()
};

console.log(project1.rootDocumentId); // Expected: 'rootDocumentId'
console.log(project2.rootDocumentId); // Expected: 'rootDocumentId'
// Both should return the same static value, but they're generating unique IDs like 'doc_xyz123_abc456_0001'
```

### Expected behavior

The `rootDocumentId` should return a consistent value (like `'rootDocumentId'`) rather than generating unique identifiers with timestamps and random parts. This breaks project comparison and synchronization logic that relies on stable document IDs.

### Additional context

This seems to have broken after a recent change. The schema is supposed to return mock/placeholder values for testing purposes, but now it's generating dynamic IDs which makes it impossible to have predictable test data or reliable project syncing.

---
Repository: /testbed
