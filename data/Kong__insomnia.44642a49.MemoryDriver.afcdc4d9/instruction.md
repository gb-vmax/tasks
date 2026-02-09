# Bug Report

### Describe the bug

There seems to be an issue with the `keys()` method in the MemoryDriver when using non-recursive listing. Keys at the base level are not being returned correctly.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some keys at different levels
await driver.setItem('base/item1', Buffer.from('data1'));
await driver.setItem('base/item2', Buffer.from('data2'));
await driver.setItem('base/nested/item3', Buffer.from('data3'));

// Try to get keys at base level only (non-recursive)
const keys = await driver.keys('base', false);

// Expected: ['base/item1', 'base/item2']
// Actual: ['base/nested/item3'] or empty array
```

### Expected behavior

When calling `keys('base', false)`, it should return only the keys that are directly under the `base` path (i.e., `base/item1` and `base/item2`), not the nested ones like `base/nested/item3`.

The level counting logic appears to be off by one, causing items at the correct depth to be filtered out while items at deeper levels are included (or vice versa).

### System Info
- Version: Latest from main branch

---
Repository: /testbed
