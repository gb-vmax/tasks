# Bug Report

### Describe the bug

The `removeItem` method in the plugin store is not properly awaiting the removal operation. When trying to remove a plugin data item, the function returns immediately without waiting for the database operation to complete, which can cause race conditions and data inconsistency issues.

### Reproduction

```js
const store = plugin.store;

// Try to remove an item and immediately check if it's gone
await store.removeItem('myKey');
const value = await store.getItem('myKey');

// Expected: null
// Actual: The value might still be present because removal hasn't completed
console.log(value); // May still return the old value
```

### Expected behavior

The `removeItem` method should wait for the database operation to complete before returning, ensuring that subsequent operations see the updated state. Any code that calls `removeItem` should be able to rely on the item being removed once the promise resolves.

### Additional context

This appears to affect plugin data persistence, particularly when plugins need to perform multiple sequential operations on the store. The lack of proper awaiting can lead to unpredictable behavior in plugin code that assumes synchronous completion after awaiting.

---
Repository: /testbed
