# Bug Report

### Describe the bug
When using the memory driver for sync storage, the `hasItem()` method is returning inverted results. It returns `false` when an item exists and `true` when an item doesn't exist.

### Reproduction
```js
const driver = new MemoryDriver();

// Set an item
await driver.setItem('myKey', Buffer.from('test data'));

// Check if item exists - returns false instead of true
const exists = await driver.hasItem('myKey');
console.log(exists); // Expected: true, Actual: false

// Check for non-existent item - returns true instead of false
const notExists = await driver.hasItem('nonExistentKey');
console.log(notExists); // Expected: false, Actual: true
```

### Expected behavior
`hasItem()` should return `true` when the key exists in storage and `false` when it doesn't exist.

### Additional context
This is causing issues with sync operations where the system thinks items don't exist when they actually do, and vice versa. Any code relying on `hasItem()` to check for the presence of stored data will behave incorrectly.

---
Repository: /testbed
