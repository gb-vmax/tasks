# Bug Report

### Describe the bug

After a recent update, the `removeItem` method in the memory driver is not working as expected. When trying to remove a regular key-value pair, the item is not being deleted from the store.

### Reproduction

```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('user:123', 'test data');

// Try to remove it
await driver.removeItem('user:123');

// Item is still there
const value = await driver.getItem('user:123');
console.log(value); // Expected: null, Actual: 'test data'
```

### Expected behavior

When calling `removeItem` with a key, the item should be deleted from the in-memory database. The method should work for both string values and Buffer objects.

### Additional context

This seems to have broken after changes were made to support wildcard patterns. Regular key deletion (without wildcards) no longer works properly.

---
Repository: /testbed
