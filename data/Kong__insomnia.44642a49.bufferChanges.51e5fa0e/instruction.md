# Bug Report

### Describe the bug

After a recent update, the database buffering system seems to have issues with multiple rapid buffer requests. When `bufferChanges()` is called multiple times in quick succession, the buffer IDs returned don't match what's expected and the flush behavior is inconsistent.

### Reproduction

```js
const bufferId1 = await database.bufferChanges(1000);
const bufferId2 = await database.bufferChanges(1000);
const bufferId3 = await database.bufferChanges(1000);

console.log(bufferId1); // Expected: 1
console.log(bufferId2); // Expected: 2  
console.log(bufferId3); // Expected: 3
```

The buffer IDs being returned are not incrementing properly. It looks like `bufferId1` might be 1, but then `bufferId2` is also 1 instead of 2, and `bufferId3` is 2 instead of 3.

### Expected behavior

Each call to `bufferChanges()` should return a unique, incrementing buffer ID. The sequence should be 1, 2, 3, etc. for consecutive calls.

### Additional context

This is affecting our ability to track which buffer operations are being flushed. The old behavior worked correctly where each call would increment the ID counter properly.

---
Repository: /testbed
