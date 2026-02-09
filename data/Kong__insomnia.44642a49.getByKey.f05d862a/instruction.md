# Bug Report

### Describe the bug

After updating plugin data using `setValueForKey`, subsequent calls to `getByKey` return stale/cached data instead of the updated values. The changes are persisted to the database but the getter returns the old value.

### Reproduction

```js
// Set initial value
await setValueForKey('my-plugin', 'settings', { theme: 'dark' });

// Retrieve it
let data = await getByKey('my-plugin', 'settings');
console.log(data.value); // { theme: 'dark' } ✓

// Update the value
await setValueForKey('my-plugin', 'settings', { theme: 'light' });

// Try to retrieve updated value
data = await getByKey('my-plugin', 'settings');
console.log(data.value); // Still shows { theme: 'dark' } ✗
```

### Expected behavior

`getByKey` should return the most recent value that was set, not a cached version. If I update plugin data and immediately read it back, I expect to see the new value.

### Additional context

This seems to have started happening recently. I'm working on a plugin that needs to read/write settings frequently and this is causing issues where the UI shows outdated information even though the database has the correct values.

---
Repository: /testbed
