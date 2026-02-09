# Bug Report

### Describe the bug
When using `database.bufferChanges()`, the changes are being flushed immediately instead of being delayed by the specified timeout. This causes the buffering mechanism to not work as intended, and database changes are applied right away rather than being batched.

### Reproduction
```js
// Set up some database changes
database.bufferChanges(5000); // Should buffer for 5 seconds

// Make multiple changes
await database.update(doc1);
await database.update(doc2);
await database.update(doc3);

// Changes are flushed immediately instead of after 5 seconds
// Expected: All changes batched and flushed after 5000ms
// Actual: Changes flushed right away
```

### Expected behavior
The `bufferChanges()` function should delay flushing database changes by the specified number of milliseconds (default 1000ms). Changes made during this period should be buffered and then flushed together after the timeout expires.

### Additional context
This seems to have broken recently. The buffering used to work correctly where multiple rapid changes would be batched together and applied after the timeout period. Now they're being applied immediately which defeats the purpose of the buffering mechanism.

---
Repository: /testbed
