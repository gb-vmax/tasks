# Bug Report

### Describe the bug

When trying to retrieve plugin data using `getByKey()`, the function returns incorrect results or null even when the data exists in the database. It seems like the query parameters are not matching the expected records.

### Reproduction

```js
// Store some plugin data
await storePluginData('my-plugin', 'api-key', 'secret-value');

// Try to retrieve it
const data = await getByKey('my-plugin', 'api-key');

// Returns null or wrong data, even though the record exists
console.log(data); // Expected: { plugin: 'my-plugin', key: 'api-key', value: 'secret-value' }
```

### Expected behavior

The `getByKey()` function should correctly retrieve plugin data when provided with the plugin name and key. The stored data should be returned as expected.

### Additional context

This appears to be affecting plugin data retrieval across the board. Any plugins that rely on storing and retrieving custom data are broken.

---
Repository: /testbed
