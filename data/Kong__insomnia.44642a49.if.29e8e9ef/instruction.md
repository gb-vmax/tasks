# Bug Report

### Describe the bug

After a recent update, the sync functionality seems to be broken. When trying to merge branches or find common snapshots between branches, the operation either hangs indefinitely or produces incorrect results. 

It looks like something went wrong with the root snapshot detection logic - the function that's supposed to find the common ancestor between two branches is now behaving strangely.

### Reproduction

```js
// Create two branches with some shared snapshot history
const branchA = {
  snapshots: ['snap1', 'snap2', 'snap3', 'snap4']
};

const branchB = {
  snapshots: ['snap1', 'snap2', 'snap5', 'snap6']
};

// Try to find the root snapshot (common ancestor)
const rootSnapshot = getRootSnapshot(branchA, branchB);

// Expected: 'snap2' (the most recent common snapshot)
// Actual: undefined or incorrect value
```

### Expected behavior

The function should return the most recent common snapshot between two branches. In the example above, it should return `'snap2'` since that's the last snapshot that appears in both branch histories.

### Additional context

This seems to have started happening after some changes to the VCS utility functions. The sync operations that rely on finding common snapshots are now failing or producing unexpected results.

System Info:
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
