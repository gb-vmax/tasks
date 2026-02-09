# Bug Report

### Describe the bug
The `hasItem()` method in the plugin store is returning incorrect boolean values. When checking if a plugin data item exists, it returns `true` when the item doesn't exist and `false` when it does exist - basically the opposite of what's expected.

### Reproduction
```js
// Assuming we have a plugin with name 'my-plugin'
const { store } = init(myPlugin);

// Set an item
await store.setItem('myKey', 'myValue');

// Check if item exists - returns false (should be true!)
const exists = await store.hasItem('myKey');
console.log(exists); // false

// Check for non-existent item - returns true (should be false!)
const notExists = await store.hasItem('nonExistentKey');
console.log(notExists); // true
```

### Expected behavior
- `hasItem()` should return `true` when the key exists in the plugin data store
- `hasItem()` should return `false` when the key doesn't exist

### Additional context
This is causing issues with plugins that rely on checking whether data exists before performing operations. The inverted logic makes it impossible to correctly determine if a key is present in the store.

---
Repository: /testbed
