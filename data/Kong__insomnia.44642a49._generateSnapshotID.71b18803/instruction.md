# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot generation where the snapshot IDs are not being properly generated. It seems like the hash collision resolution mechanism is causing problems - snapshots that should have different IDs are getting the same ID, or the cache is growing unbounded.

### Reproduction

```js
// Create multiple snapshots with the same parent and backend project
const state1 = [
  { blob: 'abc123', key: 'doc1', name: 'Document 1' },
  { blob: 'def456', key: 'doc2', name: 'Document 2' }
];

const state2 = [
  { blob: 'abc123', key: 'doc1', name: 'Document 1' },
  { blob: 'xyz789', key: 'doc3', name: 'Document 3' }
];

const id1 = _generateSnapshotID('parent123', 'project456', state1);
const id2 = _generateSnapshotID('parent123', 'project456', state2);

// Expected: id1 and id2 should be different
// Actual: They might be the same or collision handling breaks
```

### Expected behavior

Each unique snapshot state should generate a unique snapshot ID. The collision resolution should work correctly and the cache should be managed properly to prevent memory issues.

### Additional context

This appears to be affecting sync functionality where multiple snapshots are being created in quick succession. The cache seems to be interfering with proper ID generation.

---
Repository: /testbed
