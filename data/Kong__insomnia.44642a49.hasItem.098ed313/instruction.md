# Bug Report

### Describe the bug
The `hasItem` method in the plugin store is returning incorrect results when checking for the existence of plugin data. It appears to be checking whether items exist, but the logic seems off and it's giving false positives/negatives.

### Reproduction
```js
// Create a plugin with some data
const plugin = { name: 'test-plugin' };
const store = init(plugin).store;

// Set an item
await store.setItem('myKey', 'myValue');

// Check if item exists - this should return true
const exists = await store.hasItem('myKey');
console.log(exists); // Expected: true, but behavior is inconsistent

// Check for non-existent item
const notExists = await store.hasItem('nonExistentKey');
console.log(notExists); // Expected: false, but behavior is inconsistent
```

### Expected behavior
- `hasItem('myKey')` should return `true` when the key exists
- `hasItem('nonExistentKey')` should return `false` when the key doesn't exist

The method should reliably indicate whether a plugin data key exists in the store.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
