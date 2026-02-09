# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot generation in the VCS module. When creating snapshots with different state entries that have the same blob hashes, the system generates identical snapshot IDs even though the states are actually different. This causes snapshots to be incorrectly treated as duplicates.

### Reproduction

```js
const state1 = [
  { key: 'doc1', name: 'Document A', blob: 'abc123...' },
  { key: 'doc2', name: 'Document B', blob: 'abc123...' }
];

const state2 = [
  { key: 'doc1', name: 'Document B', blob: 'abc123...' },
  { key: 'doc2', name: 'Document A', blob: 'abc123...' }
];

// Both generate the same snapshot ID despite having different key/name combinations
const id1 = _generateSnapshotID(parentId, projectId, state1);
const id2 = _generateSnapshotID(parentId, projectId, state2);

// id1 === id2 (but they should be different!)
```

### Expected behavior

Different states should produce different snapshot IDs, even when the blob hashes are identical. The snapshot ID should take into account not just the blob content but also the keys and names of the entries to properly distinguish between different configurations.

### Additional context

This seems to happen when:
- Multiple entries share the same blob hash
- The entries have different keys or names
- The only difference between states is the key/name mapping

This is causing issues with version control where legitimate changes aren't being tracked properly because the snapshots collide.

---
Repository: /testbed
