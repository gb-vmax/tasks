# Bug Report

### Describe the bug

The `MemoryDriver.getItem()` method is returning `null` for keys that actually exist in the database. When I try to retrieve a value that I just stored, it returns `null` instead of the expected buffer.

### Reproduction

```js
const driver = new MemoryDriver();

// Store a value
await driver.setItem('test-key', Buffer.from('test-value'));

// Try to retrieve it
const result = await driver.getItem('test-key');

console.log(result); // Expected: Buffer containing 'test-value'
                     // Actual: null
```

### Expected behavior

When calling `getItem()` with a key that exists in the store, it should return the stored Buffer value, not `null`.

### System Info

- Using MemoryDriver for sync store
- This is blocking local development and testing

---
Repository: /testbed
