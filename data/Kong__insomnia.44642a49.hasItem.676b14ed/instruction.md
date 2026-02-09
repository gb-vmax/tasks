# Bug Report

### Describe the bug

The `hasItem` method in MemoryDriver is returning incorrect results. When checking if an item exists in the store, it's giving false positives/negatives and the logic seems backwards.

### Reproduction

```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('myKey', Buffer.from('test data'));

// Check if item exists - returns unexpected result
const exists = await driver.hasItem('myKey');
console.log(exists); // Should be true but behaves incorrectly
```

Also when checking for non-existent keys:

```js
// Check for key that doesn't exist
const missing = await driver.hasItem('nonExistentKey');
console.log(missing); // Should be false but returns wrong value
```

### Expected behavior

`hasItem` should return `true` when a key exists in the store (and the value is a Buffer), and `false` when the key doesn't exist or has no value.

### System Info
- Package: insomnia
- Module: sync/store/drivers/memory-driver

---
Repository: /testbed
