# Bug Report

### Describe the bug

I'm experiencing an issue with the memory driver where checking if a key exists after removing it still returns `true`. After calling `removeItem()` on a key, iterating over the object or checking for the key's presence behaves as if the key still exists in the database, even though its value should have been removed.

### Reproduction

```js
const driver = new MemoryDriver();

await driver.setItem('testKey', 'testValue');
await driver.removeItem('testKey');

// This still shows the key exists
const keys = Object.keys(driver._db);
console.log(keys.includes('testKey')); // Expected: false, Actual: true

// Or when iterating
for (const key in driver._db) {
  console.log(key); // 'testKey' still appears here
}
```

### Expected behavior

After `removeItem()` is called, the key should be completely removed from the internal database object. Checking for the key's existence should return `false`, and it shouldn't appear when iterating over the object keys.

### System Info
- Package: @insomnia/sync
- Using memory-driver for in-memory storage

---
Repository: /testbed
