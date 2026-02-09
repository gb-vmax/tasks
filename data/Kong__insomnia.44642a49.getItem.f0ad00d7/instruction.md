# Bug Report

### Describe the bug

The plugin store's `getItem()` method is not returning stored values correctly. When I try to retrieve data that was previously saved using `setItem()`, I'm always getting `null` back even though the data exists in the store.

### Reproduction

```js
// Save some data to the plugin store
await store.setItem('myKey', 'myValue');

// Try to retrieve it
const value = await store.getItem('myKey');
console.log(value); // Expected: 'myValue', Actual: null
```

### Steps to reproduce:
1. Use the plugin store to save a key-value pair with `setItem()`
2. Attempt to retrieve the same key using `getItem()`
3. The method returns `null` instead of the stored value

This is breaking all of my plugin's persistence functionality. The data appears to be saved correctly (I can see it in the database), but retrieval is completely broken.

### Expected behavior

`getItem()` should return the value that was previously stored with `setItem()` for the given key. If the key doesn't exist, then it should return `null`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
