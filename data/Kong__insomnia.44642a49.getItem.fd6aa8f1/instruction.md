# Bug Report

### Describe the bug

The memory driver is returning `null` for keys that exist in the database, while returning the actual value for keys that don't exist. This is the opposite of what should happen.

### Reproduction

```js
const driver = new MemoryDriver();

// Set a value
await driver.setItem('myKey', Buffer.from('test data'));

// Try to retrieve it
const value = await driver.getItem('myKey');
console.log(value); // Expected: Buffer containing 'test data', Actual: null

// Try to get a non-existent key
const missing = await driver.getItem('nonExistentKey');
console.log(missing); // Expected: null, Actual: undefined (or some value)
```

### Expected behavior

When retrieving an item that exists in the store, `getItem` should return the stored value. When retrieving an item that doesn't exist, it should return `null`.

### Additional context

This appears to affect all operations that rely on retrieving stored data from the memory driver. The logic seems inverted - values are only returned when the key is NOT found in the database.

---
Repository: /testbed
