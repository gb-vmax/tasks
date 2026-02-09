# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where `generateSnapshotStateMap` is returning an empty object instead of the expected snapshot state map. The function seems to be exiting early and not processing the snapshot data correctly.

### Reproduction

```js
const snapshot = {
  state: [
    { key: 'item1', value: 'data1' },
    { key: 'item2', value: 'data2' }
  ]
};

const result = generateSnapshotStateMap(snapshot);
console.log(result);
// Expected: { item1: {...}, item2: {...} }
// Actual: {}
```

### Expected behavior

The function should process the snapshot state and return a proper map object with all the entries from the snapshot state array. Instead, it's returning an empty object even when a valid snapshot is provided.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
