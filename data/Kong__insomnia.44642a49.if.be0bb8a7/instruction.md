# Bug Report

### Describe the bug

The database `remove` function appears to be broken - it's causing syntax errors and the application won't start. After a recent update, calling `database.remove()` on any document results in the app crashing.

### Reproduction

```js
const doc = await database.getById('req_123');
await database.remove(doc);
```

When trying to remove any document from the database, the application fails to load/compile. This seems to affect all document types (requests, folders, environments, etc.).

### Expected behavior

The `remove` function should successfully delete the document and any related descendants from the database without causing compilation errors. The app should continue running normally after the removal operation.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't delete any items from the database. Any help would be appreciated!

---
Repository: /testbed
