# Bug Report

### Describe the bug

The database `bufferChanges` function is not properly handling the flush callbacks after recent changes. When calling `bufferChanges` with an `onFlush` callback, the callback doesn't get executed when the buffer is flushed.

### Reproduction

```js
const bufferId = await database.bufferChanges(1000, () => {
  console.log('Flush completed');
});

// Make some database changes
await database.insert(doc);

// Wait for flush - callback never fires
```

### Expected behavior

The `onFlush` callback should be invoked when `flushChanges` is called, either after the timeout expires or when the buffer reaches max capacity.

### Additional context

This seems related to the new callback registration system. The `_executeFlushCallbacks` function is defined but it looks like it's not being called anywhere in the actual `flushChanges` method, so registered callbacks just sit in the Map and never execute.

---
Repository: /testbed
