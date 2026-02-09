# Bug Report

### Describe the bug

The `keys()` method in the memory driver is not returning the correct keys when using the `recursive` parameter. When `recursive` is set to `true`, it only returns keys at the base level instead of all nested keys. Conversely, when `recursive` is `false`, it returns all keys including nested ones.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some nested keys
await driver.setItem('base/level1/item1', Buffer.from('data1'));
await driver.setItem('base/level1/item2', Buffer.from('data2'));
await driver.setItem('base/item3', Buffer.from('data3'));

// This should return all keys but only returns base level
const allKeys = await driver.keys('base', true);
console.log(allKeys); // Expected: ['base/level1/item1', 'base/level1/item2', 'base/item3']
                      // Actual: ['base/item3']

// This should return only base level but returns everything
const baseKeys = await driver.keys('base', false);
console.log(baseKeys); // Expected: ['base/item3']
                       // Actual: ['base/level1/item1', 'base/level1/item2', 'base/item3']
```

### Expected behavior

When `recursive` is `true`, the method should return all keys including nested ones. When `recursive` is `false`, it should only return keys at the immediate level under the base path.

The behavior seems to be inverted from what the parameter name suggests.

---
Repository: /testbed
