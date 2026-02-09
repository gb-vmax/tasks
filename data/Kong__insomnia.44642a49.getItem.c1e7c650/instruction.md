# Bug Report

### Describe the bug
When trying to retrieve items from the memory driver, I'm getting `undefined` for keys that actually exist in the database. It seems like the logic for checking if an item exists is inverted - items that exist return `undefined` while non-existent keys might be returning garbage values.

### Reproduction
```js
const driver = new MemoryDriver();

// Store a value
await driver.setItem('myKey', Buffer.from('test data'));

// Try to retrieve it
const value = await driver.getItem('myKey');

console.log(value); // Expected: Buffer containing 'test data'
                    // Actual: undefined
```

### Expected behavior
`getItem()` should return the stored Buffer value when the key exists, and `null` when the key doesn't exist.

### Additional context
This appears to be affecting data synchronization functionality. Items are being stored correctly but can't be retrieved, which is breaking the sync process.

---
Repository: /testbed
