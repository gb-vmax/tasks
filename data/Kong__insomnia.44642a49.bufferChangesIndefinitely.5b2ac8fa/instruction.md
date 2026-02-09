# Bug Report

### Describe the bug

The database buffering mechanism is not working as expected. When I try to buffer database changes, the buffering doesn't seem to activate properly and changes are being flushed immediately instead of being buffered.

### Reproduction

```js
const bufferId = await database.bufferChangesIndefinitely();

// Make multiple database changes
await database.update(doc1);
await database.update(doc2);
await database.update(doc3);

// Changes are being written immediately instead of buffered
// Expected: changes should be held in buffer until explicitly flushed
```

### Expected behavior

When `bufferChangesIndefinitely()` is called, subsequent database operations should be buffered and not written to disk until the buffer is explicitly flushed. Currently, it seems like the buffering flag is not being set correctly and changes are being persisted immediately.

### Additional context

This is causing performance issues in our app when we need to make bulk updates, as each change triggers a separate write operation instead of batching them together.

---
Repository: /testbed
