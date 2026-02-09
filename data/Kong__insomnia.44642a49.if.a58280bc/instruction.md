# Bug Report

### Describe the bug

I'm experiencing an issue with branch merging where the common ancestor snapshot is not being correctly identified. When trying to merge branches that share a common history, the merge operation fails or produces unexpected results because it's not finding the proper root snapshot.

### Reproduction

```js
// Create two branches with shared history
const branchA = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot3']
};

const branchB = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot4']
};

// Try to find the common root snapshot
const rootSnapshot = getRootSnapshot(branchA, branchB);

// Expected: 'snapshot2' (the last common snapshot)
// Actual: Returns incorrect snapshot or null
```

### Expected behavior

When two branches share common snapshots in their history, `getRootSnapshot()` should return the most recent common snapshot between them. In the example above, both branches share 'snapshot1' and 'snapshot2', so it should return 'snapshot2' as the root.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our ability to properly merge branches with shared history. Any help would be appreciated!

---
Repository: /testbed
