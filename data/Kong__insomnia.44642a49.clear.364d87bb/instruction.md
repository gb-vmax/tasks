# Bug Report

### Describe the bug

The `store.clear()` method in the plugin context is not working as expected. When I call `clear()` on the plugin store, it doesn't actually clear all the stored data for the plugin. Some or all of the previously stored key-value pairs remain accessible after calling clear.

### Reproduction

```js
// In a plugin
const store = context.store;

// Store some data
await store.setItem('key1', 'value1');
await store.setItem('key2', 'value2');
await store.setItem('key3', 'value3');

// Try to clear all data
await store.clear();

// These should return undefined/null but they still return the values
const result1 = await store.getItem('key1');
const result2 = await store.getItem('key2');
console.log(result1, result2); // Still shows 'value1', 'value2'
```

### Expected behavior

After calling `store.clear()`, all stored data for the plugin should be removed. Subsequent calls to `getItem()` for any previously stored keys should return undefined or null.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
