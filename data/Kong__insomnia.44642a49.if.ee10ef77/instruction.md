# Bug Report

### Describe the bug

I'm encountering an issue with branch synchronization where the root snapshot detection seems to be broken. When comparing two branches with common snapshots, the function is not correctly identifying the common ancestor snapshot.

### Reproduction

```js
const branchA = {
  snapshots: ['snap1', 'snap2', 'snap3', 'snap4']
};

const branchB = {
  snapshots: ['snap1', 'snap2', 'snap5']
};

// Expected: should return 'snap2' (the deepest common snapshot)
// Actual: returns null or incorrect snapshot
const rootSnapshot = getRootSnapshot(branchA, branchB);
```

### Expected behavior

The function should return `'snap2'` as it's the most recent common snapshot between both branches. Instead, it's returning `null` or an incorrect value.

This is causing issues with:
- Branch merging operations
- Conflict detection
- History comparison

### Additional context

This seems to have started happening recently. The logic for finding common snapshots between branches appears to be incorrect. When I have two branches that definitely share common history, the sync system can't find their common ancestor.

---
Repository: /testbed
