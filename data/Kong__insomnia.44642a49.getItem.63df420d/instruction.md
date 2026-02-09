# Bug Report

### Describe the bug

I'm experiencing an issue with the plugin store's `getItem()` method after a recent update. When I retrieve values that were previously stored, I'm getting unexpected results - sometimes the values appear to be corrupted or have extra data prepended to them.

### Reproduction

```js
// Store a simple value
await store.setItem('myKey', 'myValue');

// Retrieve it later
const value = await store.getItem('myKey');

// Expected: 'myValue'
// Actual: Something like '__TTL__:1234567890:myValue' or parts of it
```

The issue seems to happen inconsistently, especially when:
1. Setting a value with `setItem()`
2. Retrieving it multiple times with `getItem()`
3. The returned value doesn't match what was originally stored

### Expected behavior

`getItem()` should return exactly what was stored with `setItem()`, without any modifications or additional metadata being exposed to the plugin.

### Additional context

This started happening after updating to the latest version. Previous versions worked fine and returned the exact string that was stored. The values seem to have some kind of internal format now that's leaking through to the plugin API.

---
Repository: /testbed
