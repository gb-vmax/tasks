# Bug Report

### Describe the bug

When calling `bufferChanges()` multiple times in succession, the buffer IDs returned are not incrementing correctly. It seems like the first call returns the current value and then increments, but subsequent calls should return incremented values each time.

### Reproduction

```js
const id1 = await database.bufferChanges(1000);
const id2 = await database.bufferChanges(1000);
const id3 = await database.bufferChanges(1000);

console.log(id1); // Expected: 1, Got: 0
console.log(id2); // Expected: 2, Got: 1
console.log(id3); // Expected: 3, Got: 2
```

### Expected behavior

Each call to `bufferChanges()` should return a unique, incrementing buffer ID starting from 1. The IDs appear to be off by one - each call returns the value before incrementing instead of after.

### Additional context

This is causing issues when trying to track and manage multiple buffered change operations, as the IDs don't match what's expected. The first buffer ID returned is 0 when it should probably be 1.

---
Repository: /testbed
