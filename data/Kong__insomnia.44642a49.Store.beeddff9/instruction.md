# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with the sync store where cached values are being returned incorrectly. When I update an item in the store, subsequent reads are returning stale data instead of the newly written values.

### Reproduction

```js
const store = new Store(driver);

// Write initial value
await store.setItem('user:123', { name: 'Alice', age: 25 });

// Read it back - works fine
const user1 = await store.getItem('user:123');
console.log(user1); // { name: 'Alice', age: 25 }

// Update the value
await store.setItem('user:123', { name: 'Bob', age: 30 });

// Read again - still returns old value!
const user2 = await store.getItem('user:123');
console.log(user2); // { name: 'Alice', age: 25 } - WRONG!
```

### Expected behavior

After updating an item with `setItem()`, calling `getItem()` should return the newly written value, not a cached version of the old value.

### Additional context

This seems to have started happening recently. The store appears to be caching values but not properly invalidating the cache when items are updated. This is causing serious data consistency issues in my application where users are seeing outdated information even after successful updates.

---
Repository: /testbed
