# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict handling where multiple merge conflicts are not being properly distinguished from each other. It appears that all merge conflicts are being assigned the same key identifier, which causes conflicts to overwrite each other or not be tracked individually.

### Reproduction

When there are multiple merge conflicts in a sync operation:

1. Create a scenario with multiple conflicting changes
2. Attempt to resolve merge conflicts
3. All conflicts appear to have the same key value ('key')
4. Unable to distinguish between different conflicts or resolve them individually

```js
// Example scenario:
// - File A has a conflict
// - File B has a conflict
// Both conflicts get assigned key: 'key' instead of unique identifiers
```

### Expected behavior

Each merge conflict should have a unique key identifier so they can be:
- Tracked independently
- Resolved individually
- Properly managed in the UI

Currently all conflicts share the same key which makes it impossible to handle multiple conflicts correctly.

### System Info
- Insomnia sync module
- Multiple merge conflicts scenario

---
Repository: /testbed
