# Bug Report

### Describe the bug

I'm experiencing an issue with document upserts in the database where the operation appears to hang or never complete. After a recent update, calling `database.upsert()` on existing documents seems to get stuck and the promise never resolves.

### Reproduction

```js
const doc = {
  _id: 'doc_123',
  type: 'request',
  name: 'My Request',
  modified: Date.now(),
  _version: 1
};

// This call never completes
await database.upsert(doc);
console.log('This line is never reached');
```

### Expected behavior

The upsert operation should complete successfully and the promise should resolve with the updated document. The function should either create a new document or update an existing one without hanging.

### Additional context

This seems to happen specifically when:
1. A document with the same ID already exists in the database
2. The document has version information attached

The operation just hangs indefinitely without throwing an error or resolving. I've tried waiting several minutes but it never completes.

---
Repository: /testbed
