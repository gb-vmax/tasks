# Bug Report

### Describe the bug
When using the plugin store API, I'm experiencing issues with `getItem()` returning stale/cached data after calling `setItem()` or `removeItem()`. The store doesn't seem to reflect the latest changes immediately.

### Reproduction
```js
// Set an initial value
await store.setItem('myKey', 'value1');

// Update the value
await store.setItem('myKey', 'value2');

// Get the value - sometimes returns 'value1' instead of 'value2'
const result = await store.getItem('myKey');
console.log(result); // Expected: 'value2', Got: 'value1'
```

Another scenario:
```js
// Set a value
await store.setItem('testKey', 'someValue');

// Remove it
await store.removeItem('testKey');

// Try to get it - sometimes returns 'someValue' instead of null
const result = await store.getItem('testKey');
console.log(result); // Expected: null, Got: 'someValue'
```

### Expected behavior
`getItem()` should always return the most recent value after `setItem()` or `removeItem()` operations. The store should be consistent and not return outdated data.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. Not sure if this is related to any caching changes or if I'm doing something wrong.

---
Repository: /testbed
