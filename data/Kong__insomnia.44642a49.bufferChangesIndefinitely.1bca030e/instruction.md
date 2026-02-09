# Bug Report

### Describe the bug

I'm experiencing an issue with the database buffering mechanism. When calling `bufferChangesIndefinitely()`, the buffer ID being returned doesn't increment correctly. Each call seems to return the same ID value instead of a unique incremented one.

### Reproduction

```js
const id1 = await database.bufferChangesIndefinitely();
const id2 = await database.bufferChangesIndefinitely();
const id3 = await database.bufferChangesIndefinitely();

console.log(id1, id2, id3);
// Expected: 1, 2, 3
// Actual: 1, 1, 1 (or similar - same value repeated)
```

### Expected behavior

Each call to `bufferChangesIndefinitely()` should return a unique, incrementing buffer ID. This is critical for tracking multiple buffered change sets independently.

### Additional context

This seems to have broken recently. The buffer IDs are supposed to be unique identifiers for each buffering session, but they're not incrementing properly anymore.

---
Repository: /testbed
