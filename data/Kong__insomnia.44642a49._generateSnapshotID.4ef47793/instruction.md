# Bug Report

### Describe the bug
When working with VCS snapshots, I'm noticing that snapshot IDs are being generated inconsistently. The same state with the same parent and backend project is producing different snapshot IDs on different runs, which is breaking snapshot comparison and sync functionality.

### Reproduction
```js
const state = [
  { blob: 'abc123' },
  { blob: 'abc123' },  // duplicate blob hash
  { blob: 'def456' }
];

const snapshotId1 = generateSnapshot('parent-1', 'project-1', state);
const snapshotId2 = generateSnapshot('parent-1', 'project-1', state);

// These should be identical but they're not
console.log(snapshotId1 === snapshotId2); // sometimes false
```

### Expected behavior
Generating a snapshot ID with identical inputs (parent ID, backend project ID, and state) should always produce the same hash. The snapshot ID generation should be deterministic so that the same state always results in the same ID.

### Additional context
This seems to affect sync operations where we need to compare snapshots to determine if changes have occurred. The inconsistent hashing is causing unnecessary sync conflicts and making it difficult to track actual changes vs. hash generation differences.

---
Repository: /testbed
