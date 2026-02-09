# Bug Report

### Issue with memory driver removeItem leaving undefined entries

I've noticed that after removing items from the memory store, the keys are still present in the database object but set to `undefined` instead of being completely removed. This is causing issues when iterating over the store or checking for key existence.

### Reproduction
```js
const driver = new MemoryDriver();

await driver.setItem('testKey', 'testValue');
await driver.removeItem('testKey');

// The key still exists in the internal _db object
// Expected: key should not exist
// Actual: key exists with value undefined
```

### Expected behavior
When `removeItem` is called, the key should be completely removed from the internal database object, not just set to `undefined`. This affects operations that check for key existence using methods like `Object.keys()` or `hasOwnProperty()`.

### Additional context
This behavior differs from how most storage drivers work (localStorage, IndexedDB, etc.) where removed keys are completely deleted. Having `undefined` values for removed keys can lead to unexpected behavior when enumerating keys or checking if a key exists in the store.

---
Repository: /testbed
