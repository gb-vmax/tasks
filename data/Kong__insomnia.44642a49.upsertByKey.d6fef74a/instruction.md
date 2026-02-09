# Bug Report

### Describe the bug
When using the plugin data storage API, the `upsertByKey` function appears to be storing values in the wrong fields. After calling `upsertByKey(plugin, key, value)`, the key and value seem to be swapped in the database.

### Reproduction
```js
// Try to store plugin data
await upsertByKey('my-plugin', 'apiToken', 'secret-token-123')

// When retrieving the data later
const data = await getByKey('my-plugin', 'apiToken')
// Expected: data.value === 'secret-token-123'
// Actual: data.value === 'apiToken' and data.key === 'secret-token-123'
```

### Expected behavior
The function should store the key in the `key` field and the value in the `value` field. When I call `upsertByKey('my-plugin', 'apiToken', 'secret-token-123')`, I expect:
- `key` to be `'apiToken'`
- `value` to be `'secret-token-123'`

Instead, these values appear to be reversed.

### Additional context
This is breaking plugin data persistence. Plugins that rely on storing configuration or state are unable to retrieve their data correctly because the key/value pairs are swapped.

---
Repository: /testbed
