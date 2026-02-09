# Bug Report

### Describe the bug

The `upsertByKey` function in the plugin-data model is not working correctly. When trying to store plugin data, the function fails because it's passing incorrect arguments to the `update` and `create` functions.

### Reproduction

```js
// Attempt to upsert plugin data
await upsertByKey('my-plugin', 'some-key', 'some-value');
```

When the key already exists (doc is found), the function tries to update but passes `key` as the first argument instead of the `doc` object.

When the key doesn't exist (doc is null), the function tries to create a new entry but passes `doc` (which is null/undefined) as the `plugin` parameter instead of the actual plugin string.

### Expected behavior

The function should:
1. When a doc exists: call `update(doc, { value })` 
2. When no doc exists: call `create({ plugin, key, value })`

This is breaking plugin data storage functionality and preventing plugins from persisting their configuration/state properly.

### System Info
- Package: @insomnia/insomnia
- File: packages/insomnia/src/models/plugin-data.ts

---
Repository: /testbed
