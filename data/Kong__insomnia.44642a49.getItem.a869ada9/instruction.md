# Bug Report

### Describe the bug

When using the memory driver for sync storage, calling `getItem()` on a key causes the item to be permanently deleted from storage. After retrieving a value once, subsequent calls to `getItem()` with the same key return `null` even though the item should still exist.

### Reproduction

```js
const driver = new MemoryDriver();

// Store a value
await driver.setItem('myKey', Buffer.from('test data'));

// First retrieval works
const value1 = await driver.getItem('myKey');
console.log(value1); // Expected: Buffer containing 'test data'

// Second retrieval fails
const value2 = await driver.getItem('myKey');
console.log(value2); // Expected: Buffer containing 'test data'
                     // Actual: null
```

### Expected behavior

`getItem()` should be a non-destructive read operation. The item should remain in storage and be retrievable multiple times. The current behavior makes it act like a "pop" operation instead of a "get" operation.

### Additional context

This appears to affect the memory driver specifically. The storage should maintain items until `removeItem()` is explicitly called.

---
Repository: /testbed
