# Bug Report

### Describe the bug

After a recent update, database changes are not being flushed at the expected intervals. When calling `bufferChanges()` multiple times in quick succession, the flush seems to be getting delayed or rescheduled unexpectedly, causing changes to not persist when they should.

### Reproduction

```js
// Call bufferChanges multiple times
const bufferId1 = await database.bufferChanges(1000);
const bufferId2 = await database.bufferChanges(1000);
const bufferId3 = await database.bufferChanges(1000);

// Wait for the expected flush time
await sleep(1100);

// Changes are not flushed yet, even though 1000ms has passed
```

### Expected behavior

Each call to `bufferChanges()` should schedule an independent flush after the specified delay. If I call `bufferChanges(1000)`, the changes should be flushed after approximately 1000ms, regardless of subsequent calls.

Currently it seems like subsequent calls are interfering with previous flush timers, causing changes to be held in the buffer longer than intended.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
