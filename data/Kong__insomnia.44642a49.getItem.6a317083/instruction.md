# Bug Report

### Describe the bug

The plugin store's `getItem` method is returning the wrong value. When retrieving stored plugin data, it returns the entire document object instead of just the value property.

### Reproduction

```js
const store = context.store;

// Store a value
await store.setItem('myKey', 'myValue');

// Try to retrieve the value
const result = await store.getItem('myKey');

// Expected: 'myValue'
// Actual: returns the full document object instead of just the value
console.log(result); // Shows entire doc object with metadata
```

### Expected behavior

`getItem` should return just the stored value (e.g., `'myValue'`), not the entire document object. This breaks existing plugins that expect to receive the raw value they stored.

### Additional context

This seems to have broken after a recent change. Previously `getItem` would return `doc.value` or `null`, but now it's returning the full document when a value exists.

---
Repository: /testbed
