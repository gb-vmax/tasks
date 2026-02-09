# Bug Report

### Describe the bug

I'm encountering an issue with snapshot ID generation where different snapshots are producing identical IDs even though they have different content. This is causing data integrity problems in version control operations.

### Reproduction

```js
const state1 = [
  { key: 'doc1', name: 'Request A', blob: 'abc123' },
  { key: 'doc2', name: 'Request B', blob: 'def456' }
];

const state2 = [
  { key: 'doc1', name: 'Request B', blob: 'abc123' },
  { key: 'doc2', name: 'Request A', blob: 'def456' }
];

// Both states generate the same snapshot ID
const id1 = generateSnapshotID('parent123', 'project456', state1);
const id2 = generateSnapshotID('parent123', 'project456', state2);

// id1 === id2, but they should be different!
```

### Expected behavior

Each unique state configuration should produce a unique snapshot ID. When the `key` or `name` fields differ between snapshots (even if the blob content is the same), the generated IDs should be different to properly distinguish between versions.

### Additional context

This seems to be affecting sync operations where snapshots with different metadata but same blob hashes are being treated as identical, leading to incorrect version history tracking.

---
Repository: /testbed
