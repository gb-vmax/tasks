# Bug Report

### Describe the bug

After a recent update, the `batchModifyDocs` function is now throwing validation errors when trying to batch modify documents. The function appears to have become much stricter about document validation and is rejecting operations that previously worked fine.

### Reproduction

```js
const docs = [
  { _id: 'req_1', name: 'My Request' },
  { _id: 'req_2', name: 'Another Request' }
];

await database.batchModifyDocs({
  upsert: docs,
  remove: []
});
```

This now throws an error like:
```
Error: Batch validation failed: Upsert document req_1 missing type; Upsert document req_2 missing type
```

### Expected behavior

The batch operation should work as it did before. We have existing code that creates documents without explicitly setting the `type` field, and this used to work fine. The function should either:
1. Continue to accept documents without strict validation, or
2. Be more lenient about missing fields

### Additional context

This is breaking our bulk import functionality where we generate documents programmatically. We'd have to update a lot of code to add type information to every document we create.

Is there a way to disable this validation or make it optional? It seems overly strict for a batch operation where we might be dealing with various document shapes.

---
Repository: /testbed
