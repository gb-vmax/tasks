# Bug Report

### Describe the bug

The `keys()` method in MemoryDriver is not returning any keys when a prefix is provided. It seems like keys that should match the prefix are being filtered out instead of being included in the results.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some test data
await driver.setItem('users/1', 'data1');
await driver.setItem('users/2', 'data2');
await driver.setItem('posts/1', 'data3');

// Try to get all keys with 'users/' prefix
const keys = await driver.keys('users/', false);

// Expected: ['users/1', 'users/2']
// Actual: []
console.log(keys); // Returns empty array
```

The method returns an empty array even though there are keys in the database that start with the given prefix. This breaks any functionality that relies on querying keys by prefix.

### Expected behavior

When calling `keys('users/', false)`, it should return all keys that start with the 'users/' prefix at the base level. The method should be including matching keys, not excluding them.

### System Info
- Insomnia version: latest
- Driver: MemoryDriver

---
Repository: /testbed
