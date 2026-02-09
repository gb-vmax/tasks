# Bug Report

### Snapshot ID generation issue with identical blobs but different keys/names

I've encountered an issue with snapshot ID generation in the VCS system. When two snapshots have entries with identical blob hashes but different keys or names, they're being assigned the same snapshot ID, which causes conflicts.

### Reproduction

```js
const state1 = [
  { key: 'doc1', name: 'Document A', blob: 'abc123...' },
  { key: 'doc2', name: 'Document B', blob: 'def456...' }
];

const state2 = [
  { key: 'doc1_renamed', name: 'Document A Renamed', blob: 'abc123...' },
  { key: 'doc2_renamed', name: 'Document B Renamed', blob: 'def456...' }
];

const id1 = _generateSnapshotID(parentId, projectId, state1);
const id2 = _generateSnapshotID(parentId, projectId, state2);

// id1 and id2 are the same even though keys and names differ
```

### Expected behavior

Snapshots with different entry keys or names should generate different snapshot IDs, even if the blob content is identical. This is important for tracking renames and other metadata changes.

### Current behavior

The snapshot ID only considers the blob hashes, so renaming documents or changing keys doesn't result in a new snapshot ID. This means the system can't distinguish between snapshots that differ only in metadata.

---
Repository: /testbed
