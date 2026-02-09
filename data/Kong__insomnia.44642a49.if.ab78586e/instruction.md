# Bug Report

### Describe the bug

I'm encountering an issue with branch merging where the common ancestor snapshot is being incorrectly identified. When trying to merge two branches that share a common history, the system seems to be returning the wrong snapshot, which causes merge operations to fail or produce unexpected results.

### Reproduction

```js
// Create two branches with shared history
const branchA = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot3']
};

const branchB = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot4']
};

// Try to find the root snapshot (common ancestor)
const rootSnapshot = getRootSnapshot(branchA, branchB);

// Expected: 'snapshot2' (the last common snapshot)
// Actual: Returns undefined or wrong snapshot
```

### Expected behavior

The function should return `'snapshot2'` as it's the most recent common snapshot between the two branches. Instead, it appears to be accessing an out-of-bounds index and returning an incorrect value.

### System Info

- Insomnia version: latest
- OS: macOS

This is blocking our ability to properly sync and merge branches. Any help would be appreciated!

---
Repository: /testbed
