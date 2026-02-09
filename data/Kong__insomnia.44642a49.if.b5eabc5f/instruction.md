# Bug Report

### Describe the bug

Getting unexpected behavior with the version control snapshot comparison logic. When trying to find common snapshots between two branches, the function seems to be returning incorrect results or not finding snapshots that should exist.

### Reproduction

```js
const branchA = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot3', 'snapshot4']
};

const branchB = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot5']
};

// Expected to find 'snapshot2' as the most recent common snapshot
const result = getRootSnapshot(branchA, branchB);
// But getting unexpected behavior
```

### Expected behavior

The function should correctly identify the most recent common snapshot between two branches by comparing their snapshot histories. In the example above, it should return `'snapshot2'` since that's the latest snapshot that exists in both branches.

### Additional context

This is affecting branch merging operations where we need to find the common ancestor snapshot. The logic seems to have issues with:
- Finding common snapshots when they exist at different positions in the arrays
- Handling cases where one branch has more snapshots than the other

Not sure if this is related to recent changes but it's causing problems with our sync workflow.

---
Repository: /testbed
