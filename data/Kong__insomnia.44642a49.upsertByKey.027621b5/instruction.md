# Bug Report

### Describe the bug
The `upsertByKey` function in the plugin-data model appears to have inverted logic. When a document exists, it tries to create a new one instead of updating the existing one, and when a document doesn't exist, it tries to update a non-existent document instead of creating one.

### Reproduction
```js
// First call - document doesn't exist yet
await upsertByKey('my-plugin', 'settings', 'value1');
// Expected: creates new document
// Actual: tries to update non-existent document

// Second call - document now exists
await upsertByKey('my-plugin', 'settings', 'value2');
// Expected: updates existing document
// Actual: tries to create duplicate document
```

### Expected behavior
- When a document with the given plugin/key combination doesn't exist, it should create a new one
- When a document already exists, it should update the existing one with the new value

This is causing issues when trying to persist plugin settings as the upsert operation fails in both scenarios.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
