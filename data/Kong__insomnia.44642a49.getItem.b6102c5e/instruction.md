# Bug Report

### Describe the bug
The plugin store's `getItem` method is returning the wrong value. When retrieving a stored item, instead of getting back the actual value that was stored, I'm getting the entire document object.

### Reproduction
```js
// Store a simple string value
await store.setItem('myKey', 'myValue');

// Try to retrieve it
const value = await store.getItem('myKey');

// Expected: 'myValue'
// Actual: returns the entire document object instead of just the value
console.log(value); // Shows full doc object with metadata instead of just 'myValue'
```

### Expected behavior
`getItem` should return the stored value directly (e.g., `'myValue'`), not the entire document object. This breaks plugins that expect to get back the same type of data they stored.

### System Info
- Insomnia version: latest
- Plugin API: store context

---
Repository: /testbed
