# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where cached items are being returned even after they've been updated. When I set a new value for a key, subsequent reads still return the old cached value instead of the newly written value.

### Reproduction

```js
// Set an initial value
await store.setItem('user-config', { theme: 'dark' });

// Read it back (works fine)
const config1 = await store.getItem('user-config');
console.log(config1); // { theme: 'dark' }

// Update the value
await store.setItem('user-config', { theme: 'light' });

// Read it again - still returns the old value!
const config2 = await store.getItem('user-config');
console.log(config2); // { theme: 'dark' } - Expected: { theme: 'light' }
```

### Expected behavior

When a value is updated using `setItem()` or `setItemRaw()`, the next call to `getItem()` should return the newly written value, not the stale cached version.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing data inconsistency issues in my workflows. Any help would be appreciated!

---
Repository: /testbed
