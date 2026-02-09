# Bug Report

### Describe the bug

After a recent update, I'm experiencing memory issues when using `bufferChangesIndefinitely()` in the database module. The application becomes unresponsive and eventually crashes when there are many database changes being buffered.

### Reproduction

```js
// Start buffering changes
const bufferId = await database.bufferChangesIndefinitely();

// Make a large number of database changes without flushing
for (let i = 0; i < 15000; i++) {
  await database.update(someModel, { field: `value_${i}` });
}

// App becomes unresponsive and crashes
```

### Expected behavior

The application should handle buffered changes gracefully, even when there are many changes. Previously, this worked fine and I could buffer as many changes as needed before manually flushing.

### Additional context

This seems to have started happening after the latest update. The buffer appears to be automatically flushing itself now, which is causing issues with my workflow where I need to control exactly when changes are persisted. I'm also seeing console warnings about buffer size limits that weren't there before.

The automatic flushing is particularly problematic because:
1. It happens unexpectedly during my batch operations
2. It breaks the atomicity I was relying on
3. The timing is unpredictable

Is this new auto-flush behavior intentional? If so, is there a way to disable it or increase the buffer size limit?

---
Repository: /testbed
