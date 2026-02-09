# Bug Report

### Describe the bug

When trying to find the common root snapshot between two branches, I'm getting the wrong snapshot returned. It seems like the function is returning a snapshot that's one position off from what it should be.

### Reproduction

```js
const branchA = {
  snapshots: ['snap1', 'snap2', 'snap3', 'snap4']
};

const branchB = {
  snapshots: ['snap1', 'snap2', 'snap5', 'snap6']
};

// Expected: 'snap2' (the last common snapshot)
// Actual: Returns 'snap3' instead
const root = getRootSnapshot(branchA, branchB);
```

The function appears to be returning the snapshot immediately after the common one, rather than the actual common snapshot itself. This causes issues when trying to merge branches or determine the correct base for comparisons.

### Expected behavior

`getRootSnapshot()` should return the most recent snapshot that exists in both branches. In the example above, it should return `'snap2'` since that's the last snapshot common to both branches.

### System Info
- Package: insomnia
- Module: sync/vcs/util.ts

---
Repository: /testbed
