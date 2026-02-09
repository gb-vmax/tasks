# Bug Report

### Describe the bug

After a recent update, the plugin store's `getItem()` method is returning parsed JSON objects instead of strings. This is breaking plugins that expect string values from the store.

### Reproduction

```js
// In a plugin
await context.store.setItem('myKey', '{"foo": "bar"}');
const value = await context.store.getItem('myKey');

// Expected: '{"foo": "bar"}' (string)
// Actual: { foo: 'bar' } (parsed object)
```

The store is now automatically parsing JSON strings, which changes the return type. This wasn't happening before and breaks existing plugins that rely on getting back the exact string value that was stored.

### Expected behavior

`getItem()` should return the same string value that was stored with `setItem()`, without any automatic JSON parsing. The plugin should be responsible for parsing if needed.

### Additional context

This seems to have started after some caching changes were made to the store implementation. The previous behavior was consistent - strings in, strings out.

---
Repository: /testbed
