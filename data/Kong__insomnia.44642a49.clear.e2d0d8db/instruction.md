# Bug Report

### Describe the bug

The `MemoryDriver.clear()` method doesn't actually clear the in-memory database. After calling `clear()`, all previously stored data is still accessible, which breaks the expected behavior of clearing the store.

### Reproduction

```js
const driver = new MemoryDriver();

// Store some data
await driver.setItem('key1', 'value1');
await driver.setItem('key2', 'value2');

// Try to clear the store
await driver.clear();

// Data is still there!
const value = await driver.getItem('key1');
console.log(value); // Expected: null, Actual: 'value1'
```

### Expected behavior

After calling `clear()`, the memory store should be empty and all previously stored keys should return `null` when accessed.

### System Info
- insomnia version: latest
- OS: macOS

---
Repository: /testbed
