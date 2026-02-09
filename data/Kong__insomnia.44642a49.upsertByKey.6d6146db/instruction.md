# Bug Report

### Describe the bug

Plugin data storage is not working correctly - values are being stored in the wrong fields. When I try to save plugin configuration data using the API, the key and value parameters seem to be swapped or incorrectly assigned.

### Reproduction

```js
// Trying to store plugin data
await upsertByKey('my-plugin', 'apiToken', 'secret-value-123');

// Expected: key='apiToken', value='secret-value-123'
// Actual: The data is stored incorrectly
```

When I retrieve the data afterwards, I'm getting the key where the value should be, and the value where the key should be. This makes it impossible to properly store and retrieve plugin configuration.

### Expected behavior

The `upsertByKey` function should store the key in the `key` field and the value in the `value` field. When I call `upsertByKey('my-plugin', 'setting-name', 'setting-value')`, I expect:
- `key` field to contain `'setting-name'`
- `value` field to contain `'setting-value'`

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking plugin data persistence for my custom plugin. Any help would be appreciated!

---
Repository: /testbed
