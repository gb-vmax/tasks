# Bug Report

### Describe the bug
The plugin store's `getItem()` method is returning `null` when data exists and returning `undefined` when no data is found. This is the opposite of what should happen - it should return the stored value when data exists and `null` when it doesn't.

### Reproduction
```js
// Store some data
await store.setItem('myKey', 'myValue');

// Try to retrieve it
const value = await store.getItem('myKey');
console.log(value); // Expected: 'myValue', Actual: null

// Try to get non-existent key
const missing = await store.getItem('nonExistent');
console.log(missing); // Expected: null, Actual: undefined
```

### Expected behavior
- `getItem()` should return the stored value when the key exists
- `getItem()` should return `null` when the key doesn't exist

### System Info
- Insomnia version: latest
- Plugin API version: current

This is breaking plugin functionality that relies on persistent storage. Any plugins that store and retrieve data are affected.

---
Repository: /testbed
