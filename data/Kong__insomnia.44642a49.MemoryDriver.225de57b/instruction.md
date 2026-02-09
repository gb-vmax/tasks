# Bug Report

### Describe the bug
When using the memory driver to remove items with a prefix, the `removeItems()` method doesn't actually remove anything. It appears to be skipping over all the keys that match the prefix instead of removing them.

### Reproduction
```js
const driver = new MemoryDriver();

// Add some items with a prefix
await driver.setItem('workspace/item1', Buffer.from('data1'));
await driver.setItem('workspace/item2', Buffer.from('data2'));
await driver.setItem('other/item3', Buffer.from('data3'));

// Try to remove all items with 'workspace/' prefix
await driver.removeItems('workspace/');

// Items with 'workspace/' prefix are still there
const item1 = await driver.getItem('workspace/item1'); // Should be null but isn't
const item2 = await driver.getItem('workspace/item2'); // Should be null but isn't
const item3 = await driver.getItem('other/item3'); // Should still exist
```

### Expected behavior
The `removeItems()` method should remove all items that start with the given prefix. In the example above, `workspace/item1` and `workspace/item2` should be removed, but `other/item3` should remain.

Currently it seems like the method is doing the opposite - keeping items that match the prefix and potentially removing items that don't match.

---
Repository: /testbed
