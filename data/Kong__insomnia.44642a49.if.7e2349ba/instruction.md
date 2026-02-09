# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database inserts failing silently or returning undefined. It seems like documents are not being properly inserted into the database, and in some cases the insert operation just hangs without resolving or rejecting.

### Reproduction

```js
const doc = {
  _id: 'test_123',
  type: 'request',
  created: Date.now(),
  modified: Date.now(),
  name: 'My Request'
};

// This insert operation doesn't work as expected
const result = await database.insert(doc);
console.log(result); // Expected: inserted document, Actual: undefined or hangs
```

### Expected behavior

The `insert` method should properly insert the document into the database and return the newly inserted document with all its properties. The promise should resolve with the document data.

### Additional context

This seems to have started happening recently. The insert function appears to have some duplicate code or malformed structure that's preventing it from executing correctly. Documents that should be inserted successfully are either not being inserted at all, or the function is not returning the expected result.

---
Repository: /testbed
