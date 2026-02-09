# Bug Report

### Describe the bug

Database changes are not being buffered properly when using `bufferChangesIndefinitely()`. After calling this function, subsequent database operations are immediately persisted instead of being buffered as expected.

### Reproduction

```js
// Call bufferChangesIndefinitely to start buffering
const bufferId = await database.bufferChangesIndefinitely();

// Make some database changes
await database.update(doc1);
await database.update(doc2);

// Changes are written immediately instead of being buffered
// Expected: changes should be held in memory until buffer is flushed
```

### Expected behavior

When `bufferChangesIndefinitely()` is called, all subsequent database operations should be buffered in memory and not persisted until the buffer is explicitly flushed or released. Currently, the changes are being written immediately, defeating the purpose of the buffering mechanism.

This is causing performance issues in scenarios where we need to batch multiple database operations together.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
