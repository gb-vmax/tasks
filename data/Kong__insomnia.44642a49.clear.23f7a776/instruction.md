# Bug Report

### Describe the bug
The `clear()` method in the memory driver doesn't actually clear the database. After calling `clear()`, all previously stored keys and values remain accessible.

### Reproduction
```js
const driver = new MemoryDriver();

// Add some data
await driver.setItem('key1', 'value1');
await driver.setItem('key2', 'value2');

// Try to clear
await driver.clear();

// Keys still exist
const keys = await driver.keys('', true);
console.log(keys); // Expected: [], Actual: ['key1', 'key2']
```

### Expected behavior
After calling `clear()`, the memory driver should reset its internal database and all keys should be removed. Subsequent calls to `keys()` should return an empty array.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
