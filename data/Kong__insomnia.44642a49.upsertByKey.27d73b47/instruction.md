# Bug Report

### Describe the bug

When using plugin data storage, the `upsertByKey` function is not storing the correct values. Instead of saving the actual data value, it appears to be storing incorrect data - either the plugin name or the key name depending on whether it's an update or create operation.

### Reproduction

```js
// Try to store plugin data
await upsertByKey('my-plugin', 'setting-key', 'actual-value-to-store');

// Retrieve the data
const data = await getByKey('my-plugin', 'setting-key');

// Expected: data.value === 'actual-value-to-store'
// Actual: data.value === 'my-plugin' (if updating) or 'setting-key' (if creating)
```

### Steps to reproduce:
1. Call `upsertByKey` with a plugin name, key, and value
2. Retrieve the stored data using `getByKey`
3. Check the returned value - it will be wrong

### Expected behavior

The function should store the provided `value` parameter in the database, not the plugin name or key.

### Additional context

This is breaking plugin configuration persistence. Any plugin that tries to save settings using this API will get corrupted data back when retrieving it later.

---
Repository: /testbed
