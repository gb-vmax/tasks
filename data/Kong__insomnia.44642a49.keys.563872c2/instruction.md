# Bug Report

### Describe the bug

The `keys()` method in the memory driver is returning incorrect results when filtering by prefix. It seems like keys that should match the prefix are being excluded, while keys that don't match might be included.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some test data
await driver.setItem('users/1/profile', 'data1');
await driver.setItem('users/2/profile', 'data2');
await driver.setItem('settings/theme', 'data3');

// Try to get all keys with 'users/' prefix
const keys = await driver.keys('users/', false);

// Expected: ['users/1/profile', 'users/2/profile']
// Actual: returns empty array or incorrect keys
console.log(keys);
```

When calling `keys()` with a specific prefix, the method doesn't return the keys that start with that prefix. This breaks functionality that depends on querying keys by prefix pattern.

### Expected behavior

The `keys()` method should return all keys that start with the given prefix. When `recursive` is false, it should only return keys at the immediate level below the prefix. When `recursive` is true, it should return all nested keys under that prefix.

### System Info
- Package: @insomnia/sync
- Component: MemoryDriver

---
Repository: /testbed
