# Bug Report

### Describe the bug

The plugin store's `hasItem()` method is not properly invalidating its cache when items are added or removed. After calling `setItem()` or `removeItem()`, subsequent calls to `hasItem()` for the same key still return stale cached values instead of reflecting the actual current state.

### Reproduction

```js
// Set an item
await store.setItem('myKey', 'myValue');

// Check if it exists - returns true (correct)
const exists1 = await store.hasItem('myKey');
console.log(exists1); // true

// Remove the item
await store.removeItem('myKey');

// Check again - still returns true from cache (incorrect!)
const exists2 = await store.hasItem('myKey');
console.log(exists2); // true (should be false)
```

Similarly, if you check for a non-existent key, then add it, `hasItem()` continues to return `false`:

```js
// Check for non-existent key
const exists1 = await store.hasItem('newKey');
console.log(exists1); // false

// Add the key
await store.setItem('newKey', 'value');

// Check again - still returns false from cache (incorrect!)
const exists2 = await store.hasItem('newKey');
console.log(exists2); // false (should be true)
```

### Expected behavior

The `hasItem()` method should always return the current state of whether a key exists in the store, regardless of caching. The cache should be invalidated when `setItem()` or `removeItem()` operations modify the store.

### System Info
- Insomnia version: latest
- Plugin API: store context

---
Repository: /testbed
