# Bug Report

### Describe the bug

The plugin store's `getItem` method is returning the entire document object instead of just the value. This breaks plugins that rely on retrieving stored values.

### Reproduction

```js
const store = context.store;

// Store a value
await store.setItem('myKey', 'myValue');

// Try to retrieve it
const value = await store.getItem('myKey');

// Expected: 'myValue'
// Actual: returns the entire document object instead of just the value
console.log(value); // outputs document object with metadata instead of 'myValue'
```

### Expected behavior

`getItem` should return the stored value (or null if not found), not the entire document object. This is the standard behavior for key-value storage APIs.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
