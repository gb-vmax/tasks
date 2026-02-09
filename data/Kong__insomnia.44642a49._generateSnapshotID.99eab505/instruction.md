# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot ID generation in the VCS module. When creating snapshots with the same state but different parent/project combinations, the generated IDs are inconsistent. It seems like snapshots that should have different IDs are sometimes getting the same ID, and vice versa.

### Reproduction

```js
const state = [
  { blob: 'abc123' },
  { blob: 'def456' }
];

// These should generate different snapshot IDs
const id1 = _generateSnapshotID('parent1', 'project1', state);
const id2 = _generateSnapshotID('project1', 'parent1', state);

// But they might be the same when they shouldn't be
```

Also noticed that when the state array contains entries with identical blob values, the sorting doesn't work as expected and the snapshot ID generation becomes unreliable.

### Expected behavior

- Snapshot IDs should be unique for different parent/project combinations
- The state sorting should properly handle cases where blob values are equal
- Swapping parent and project IDs should result in different snapshot hashes

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
