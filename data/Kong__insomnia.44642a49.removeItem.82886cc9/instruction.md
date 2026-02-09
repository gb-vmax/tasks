# Bug Report

### Describe the bug
After a recent update, the plugin store's `removeItem()` method is creating unexpected entries in the database with keys prefixed by `__deleted__`. When I delete an item from the plugin store, instead of just removing it, the system is now storing a copy of the deleted item with a timestamped deletion key.

### Reproduction
```js
// Using the plugin store API
await store.setItem('myKey', { data: 'test value' });
await store.removeItem('myKey');

// After calling removeItem, there's now an entry like:
// Key: "__deleted__1234567890:myKey"
// Value: { data: 'test value' }

// The original key is removed, but this deletion tracking entry remains
```

### Expected behavior
When `removeItem()` is called, the item should be completely removed from the store without creating any additional entries. The store should not be cluttered with deletion tracking keys.

### Additional context
This appears to be some kind of soft-delete mechanism that was added, but it's causing issues:
1. The store is accumulating these `__deleted__` entries over time
2. It's not clear why deleted items need to be preserved
3. There's cleanup logic that runs on every `removeItem()` call which seems inefficient

Is this intended behavior? If so, what's the purpose of keeping deleted items around?

---
Repository: /testbed
