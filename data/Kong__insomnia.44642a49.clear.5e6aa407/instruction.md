# Bug Report

### Describe the bug

After a recent update, the plugin store's `clear()` method is behaving unexpectedly. Instead of completely clearing all stored data for a plugin, it seems to be leaving behind some entries with keys that start with `__backup_`.

### Reproduction

```js
// In a plugin
const store = context.store;

// Set some data
await store.setItem('config', { setting: 'value' });
await store.setItem('cache', { data: 'test' });

// Clear all data
await store.clear();

// Try to get all items
const items = await store.all();

console.log(items); // Expected: empty array, but contains backup entries
```

### Expected behavior

When calling `store.clear()`, all plugin data should be removed completely. The store should be empty after clearing, with no leftover entries.

### Additional context

This is causing issues when plugins try to reset their state. The backup entries accumulate over time and aren't cleaned up, which can lead to storage bloat. It looks like the clear method is creating backup entries but never removing them, which defeats the purpose of having a clear function.

---
Repository: /testbed
