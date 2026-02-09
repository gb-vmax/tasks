# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database change buffering when `bufferChangesIndefinitely()` is called multiple times in succession. The buffer seems to be flushing prematurely even though it's supposed to buffer changes indefinitely.

### Reproduction

```js
// Create multiple indefinite buffers
const bufferId1 = await database.bufferChangesIndefinitely();
const bufferId2 = await database.bufferChangesIndefinitely();
const bufferId3 = await database.bufferChangesIndefinitely();

// Make changes that should be buffered
await database.update(doc1);
await database.update(doc2);
// ... more updates

// Changes are being flushed unexpectedly before flushChanges is called
```

### Expected behavior

When using `bufferChangesIndefinitely()`, changes should remain buffered until `flushChanges()` is explicitly called with the corresponding buffer ID. The buffer should not automatically flush just because multiple buffer IDs are created or a certain number of changes accumulate.

### Additional context

This seems to have started happening after the change buffer size limit was introduced. The indefinite buffering behavior should not be affected by the `MAX_BUFFER_SIZE` constant - that's the whole point of "indefinite" buffering.

---
Repository: /testbed
