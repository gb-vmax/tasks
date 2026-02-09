# Bug Report

### Describe the bug
The `clear()` method in the memory driver is not working as expected. When I try to clear the in-memory database, nothing happens and all the stored data remains intact.

### Reproduction
```js
const driver = new MemoryDriver();

// Store some data
await driver.setItem('key1', 'value1');
await driver.setItem('key2', 'value2');

// Try to clear all data
await driver.clear();

// Data is still there!
const value = await driver.getItem('key1');
console.log(value); // Still returns 'value1' instead of undefined
```

### Expected behavior
After calling `clear()`, all stored items should be removed from the memory driver. Subsequent calls to `getItem()` should return `undefined` for previously stored keys.

### Additional context
This seems to have broken recently. The clear method used to work fine but now it just doesn't do anything. I'm using this for testing and need to reset the state between tests, but the old data keeps persisting.

---
Repository: /testbed
