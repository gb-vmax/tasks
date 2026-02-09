# Bug Report

### Describe the bug

When using the memory driver for storage, calling `removeItem()` doesn't actually remove the key from the database object. Instead, it sets the value to `undefined`, which means the key still exists in the object.

### Reproduction

```js
const driver = new MemoryDriver();

// Set a value
await driver.setItem('myKey', 'myValue');

// Remove the item
await driver.removeItem('myKey');

// The key still exists in the object
console.log('myKey' in driver._db); // Expected: false, Actual: true
console.log(Object.keys(driver._db)); // Expected: [], Actual: ['myKey']
```

### Expected behavior

After calling `removeItem()`, the key should be completely removed from the database object. Checking if the key exists should return `false`, and the key should not appear when iterating over the object's keys.

### System Info
- Package: @insomnia/sync

---
Repository: /testbed
