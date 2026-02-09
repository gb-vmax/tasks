# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot ID generation in the VCS module. When creating snapshots with identical state but different ordering, the generated snapshot IDs are inconsistent. This is causing problems with version control operations where snapshots that should be considered equivalent are being treated as different.

Additionally, it seems like the last entry in the state array is being ignored when generating the snapshot ID, which means snapshots with different final entries can sometimes produce the same ID.

### Reproduction

```js
const state1 = [
  { blob: 'blob-a' },
  { blob: 'blob-b' },
  { blob: 'blob-c' }
];

const state2 = [
  { blob: 'blob-a' },
  { blob: 'blob-b' },
  { blob: 'blob-d' }  // Different last entry
];

// These produce the same snapshot ID even though state is different
const id1 = _generateSnapshotID('parent1', 'project1', state1);
const id2 = _generateSnapshotID('parent1', 'project1', state2);

console.log(id1 === id2); // true (unexpected!)
```

Also, swapping the parent and project IDs produces different snapshot IDs:

```js
const id3 = _generateSnapshotID('parent1', 'project1', state1);
const id4 = _generateSnapshotID('project1', 'parent1', state1);

console.log(id3 === id4); // false (unexpected!)
```

### Expected behavior

1. All entries in the state array should be included in the hash calculation
2. The order of parent ID and backend project ID in the hash should be consistent with the rest of the codebase
3. Snapshots with identical state should always produce the same ID regardless of input parameter ordering

This is affecting our ability to properly track changes and is causing duplicate snapshots to be created in some cases.

---
Repository: /testbed
