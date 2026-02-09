# Bug Report

### Describe the bug

After a recent update, the `hasItem()` method in the memory driver is not working correctly. When checking if an item exists in the store, it always returns `false` even for items that were just added.

### Reproduction

```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('myKey', Buffer.from('test data'));

// Check if item exists - this returns false but should return true
const exists = await driver.hasItem('myKey');
console.log(exists); // Expected: true, Actual: false
```

### Expected behavior

`hasItem()` should return `true` when an item exists in the store and hasn't expired. Items without an expiration should always be considered valid.

### Additional context

This seems to have started happening after some changes to the memory driver. The basic set/get operations appear to be affected when checking for item existence.

---
Repository: /testbed
