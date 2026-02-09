# Bug Report

### Describe the bug

The `hasItem()` method in the memory driver is returning incorrect results. When checking if a key exists in the store, it's returning `true` for keys that don't actually exist.

### Reproduction

```js
const driver = new MemoryDriver();

// Check for a key that was never set
const exists = await driver.hasItem('nonexistent-key');

// Expected: false
// Actual: true
```

### Expected behavior

`hasItem()` should return `false` when a key doesn't exist in the store. Currently it's returning `true` even for keys that were never set, which breaks the logic for checking whether data exists before trying to retrieve it.

### Additional context

This is causing issues with sync operations where we need to know if a key exists before attempting to read or update it. The method should only return `true` if the key actually has a Buffer value stored.

---
Repository: /testbed
