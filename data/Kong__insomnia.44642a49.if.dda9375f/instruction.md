# Bug Report

### Describe the bug

When upserting documents in the database, the `upsert` method is not working correctly. The function definition seems malformed - there's a standalone function definition appearing before the actual method, and the method signature is broken.

### Reproduction

```js
const doc = {
  _id: 'test-123',
  type: 'request',
  name: 'My Request',
  modified: Date.now()
};

// Try to upsert a document
await database.upsert(doc);
```

### Expected behavior

The `upsert` method should execute successfully, either inserting a new document or updating an existing one without syntax errors.

### Actual behavior

The code fails to execute due to malformed function structure. The helper functions `_detectUpsertConflict` and `_resolveUpsertConflict` are defined outside of any containing scope, appearing between the old function body and the new method definition.

### Additional context

This appears to have broken after a recent change to add conflict detection logic. The function structure needs to be fixed - either the helper functions should be defined inside the method, moved outside the database object entirely, or the method definition needs proper formatting.

---
Repository: /testbed
