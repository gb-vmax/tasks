# Bug Report

### Describe the bug

When using the MemoryDriver with the `keys()` method and `recursive: false`, it's returning keys from nested directories instead of only returning keys from the base level. The behavior seems inverted - non-recursive calls are acting like recursive calls.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some nested keys
await driver.setItem('base/item1', Buffer.from('data1'));
await driver.setItem('base/nested/item2', Buffer.from('data2'));
await driver.setItem('base/nested/deep/item3', Buffer.from('data3'));

// Try to get only base-level keys (non-recursive)
const baseKeys = await driver.keys('base/', false);

// Expected: ['base/item1']
// Actual: Returns nested keys that should be excluded
```

### Expected behavior

When calling `keys()` with `recursive: false`, it should only return keys at the immediate level under the specified base path, not keys from nested subdirectories.

### System Info
- Package: @insomnia/sync
- Component: MemoryDriver

---
Repository: /testbed
