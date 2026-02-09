# Bug Report

### Describe the bug

After a recent update, the `generateSnapshotStateMap` function appears to be broken. When I call it with a valid snapshot object, it returns an empty object `{}` instead of the expected state map.

### Reproduction

```js
const snapshot = {
  state: [
    { key: 'doc1', name: 'Document 1', blob: '...' },
    { key: 'doc2', name: 'Document 2', blob: '...' }
  ]
};

const stateMap = generateSnapshotStateMap(snapshot);
console.log(stateMap);
// Expected: { doc1: { key: 'doc1', name: 'Document 1', ... }, doc2: { ... } }
// Actual: {}
```

### Expected behavior

The function should return a proper state map with all the entries from the snapshot indexed by their keys. Instead it's returning an empty object even when the snapshot has valid state entries.

This is causing issues with syncing as the state map is used throughout the sync process to look up documents by key.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
