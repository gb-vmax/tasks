# Bug Report

### Describe the bug

I'm experiencing an issue with plugin data persistence where updates to plugin data don't seem to be reflected when retrieving the data immediately after. The data appears to be cached or stale, causing the old values to be returned instead of the newly updated ones.

### Reproduction

```js
// Set initial plugin data
await upsertByKey('my-plugin', 'config', 'initial-value');

// Retrieve the data - works fine
const data1 = await getByKey('my-plugin', 'config');
console.log(data1.value); // 'initial-value'

// Update the data
await upsertByKey('my-plugin', 'config', 'updated-value');

// Retrieve again - still returns old value
const data2 = await getByKey('my-plugin', 'config');
console.log(data2.value); // Expected: 'updated-value', Actual: 'initial-value'
```

### Expected behavior

After updating plugin data with `upsertByKey`, subsequent calls to `getByKey` should return the updated value, not the stale/cached value.

### Additional context

This seems to have started happening recently. The updates are being saved to the database correctly (I can see them after restarting the app), but within the same session, the old values persist when querying.

---
Repository: /testbed
