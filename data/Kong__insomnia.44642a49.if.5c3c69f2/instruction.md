# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with branch synchronization. When trying to find the common ancestor between two branches, the function seems to be returning `null` or an empty string instead of the actual common snapshot ID.

### Reproduction

```js
const branchA = {
  snapshots: ['snap1', 'snap2', 'snap3']
};

const branchB = {
  snapshots: ['snap1', 'snap4', 'snap5']
};

// Expected: 'snap1' (the common snapshot)
// Actual: null or empty string
const commonSnapshot = getRootSnapshot(branchA, branchB);
```

### Expected behavior

The function should return the most recent common snapshot ID between the two branches. In the example above, it should return `'snap1'` since that's the shared snapshot between both branches.

### Additional context

This is affecting our ability to merge branches properly. The sync operation fails because it can't identify the common base snapshot to work from. It worked fine in the previous version but started happening after the latest changes.

---
Repository: /testbed
