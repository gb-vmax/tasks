# Bug Report

### Describe the bug

After a recent update, plugin data storage is behaving strangely. When I retrieve stored values using the plugin API, I'm getting back values with weird prefixes like `__v1__:` or `__v2__:` instead of the actual data I stored.

### Reproduction

```js
// Store a value
await pluginData.set('my-plugin', 'user-token', 'abc123');

// Retrieve the value
const token = await pluginData.get('my-plugin', 'user-token');

// Expected: 'abc123'
// Actual: '__v1__:abc123'
```

If I update the value multiple times, the version number keeps incrementing:

```js
await pluginData.set('my-plugin', 'counter', '1');
await pluginData.set('my-plugin', 'counter', '2');
const value = await pluginData.get('my-plugin', 'counter');

// Expected: '2'
// Actual: '__v2__:2'
```

### Expected behavior

The plugin data API should return the raw values that were stored, without any internal versioning prefixes. These prefixes appear to be an implementation detail that shouldn't be exposed to plugin developers.

### Additional context

This is breaking plugins that rely on exact string matching or parsing of stored values. The versioning system seems to be leaking through the public API when it should be handled internally.

---
Repository: /testbed
