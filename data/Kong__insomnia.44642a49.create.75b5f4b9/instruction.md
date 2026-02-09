# Bug Report

### Describe the bug

When creating a new plugin data entry using the `create()` function with a patch object, the patch properties are not being properly persisted to the database. The returned object includes the patch properties, but they don't actually get saved.

### Reproduction

```js
const pluginData = create({
  pluginId: 'my-plugin',
  key: 'some-key',
  value: 'some-value'
});

// The returned object has the properties
console.log(pluginData.pluginId); // 'my-plugin'
console.log(pluginData.key); // 'some-key'

// But if you fetch it from the database later, the patch properties are missing
// Only the default properties from db.docCreate() are actually saved
```

### Expected behavior

The `create()` function should persist all properties from the patch object to the database, not just merge them into the returned object. The patch should be passed to `db.docCreate()` so the properties are actually saved.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
