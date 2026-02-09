# Bug Report

### Describe the bug

The plugin store's `hasItem()` method is returning incorrect values. When checking if a key exists in the plugin data store, it returns `true` when the item doesn't exist and `false` when it does exist - basically the opposite of what it should return.

### Reproduction

```js
const plugin = {
  name: 'my-plugin'
};

const { store } = init(plugin);

// Store some data
await store.setItem('test-key', 'test-value');

// Check if item exists - returns false even though it exists
const exists = await store.hasItem('test-key');
console.log(exists); // Expected: true, Actual: false

// Check for non-existent key - returns true even though it doesn't exist
const notExists = await store.hasItem('non-existent-key');
console.log(notExists); // Expected: false, Actual: true
```

### Expected behavior

`hasItem()` should return `true` when a key exists in the store and `false` when it doesn't exist.

### Additional context

This is breaking plugin functionality that relies on checking whether data exists before performing operations. Any plugins using `hasItem()` to check for existing data will get inverted results.

---
Repository: /testbed
