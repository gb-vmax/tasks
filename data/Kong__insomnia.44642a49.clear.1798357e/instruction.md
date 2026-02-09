# Bug Report

### Describe the bug
The `clear()` method on the Store class is not working as expected. Instead of clearing the store data, it appears to be returning the driver object itself when the driver exists, which means the store never actually gets cleared.

### Reproduction
```js
const store = new Store(driver);

// Add some data to the store
await store.set('key1', 'value1');
await store.set('key2', 'value2');

// Try to clear the store
await store.clear();

// Check if data still exists
const value = await store.get('key1');
console.log(value); // Expected: undefined, Actual: 'value1'
```

### Expected behavior
Calling `store.clear()` should remove all data from the store. After clearing, any subsequent `get()` calls should return `undefined` for previously set keys.

### Actual behavior
The store data is not being cleared. All previously stored values remain accessible after calling `clear()`.

### System Info
- Package: insomnia
- Version: latest
- Module: sync/store

---
Repository: /testbed
