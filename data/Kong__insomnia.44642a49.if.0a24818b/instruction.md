# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state processing where duplicate keys in the state array are causing unexpected behavior. When `generateStateMap` processes a `SnapshotState` array, it seems to be creating duplicate entries or not handling the state correctly.

### Reproduction

```js
const state = [
  { key: 'doc1', blob: 'abc123', name: 'Document 1' },
  { key: 'doc2', blob: 'def456', name: 'Document 2' },
  { key: 'doc1', blob: 'xyz789', name: 'Document 1 Updated' }
];

const stateMap = generateStateMap(state);

// Expected: stateMap should contain only 2 entries with 'doc1' being the latest
// Actual: Getting unexpected results or errors
```

### Expected behavior

The function should properly convert the snapshot state array into a map, handling duplicate keys appropriately. When the same key appears multiple times, it should keep the correct entry based on the blob comparison logic.

### System Info
- Insomnia version: latest
- OS: macOS

The state map generation appears to be broken after a recent change. It looks like there might be some duplicate code or incorrect logic in the function implementation.

---
Repository: /testbed
