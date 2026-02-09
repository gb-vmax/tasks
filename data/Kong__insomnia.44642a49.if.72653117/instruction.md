# Bug Report

### Describe the bug

I'm experiencing an issue with the `withDescendants` function in the database module. When trying to fetch a document with its descendants, the function seems to be returning incorrect results or potentially hanging/not returning the expected data structure.

### Reproduction

```js
const doc = await database.get('some-document-id');
const descendants = await database.withDescendants(doc);

// Expected: doc + all its child/descendant documents
// Actual: returns unexpected results or wrong document set
```

### Steps to reproduce
1. Create a document hierarchy (parent with multiple child documents)
2. Call `withDescendants` on the parent document
3. Observe that the returned array doesn't contain the expected descendants

### Expected behavior
The function should return an array containing the original document plus all of its descendant documents in the hierarchy, stopping at the specified `stopType` if provided.

### Additional context
This seems to have started happening recently. The function appears to work when the database is in a certain state but fails in others. Not sure if this is related to the database initialization or some other internal state.

---
Repository: /testbed
