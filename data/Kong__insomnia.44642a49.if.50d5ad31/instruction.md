# Bug Report

### Describe the bug

I'm experiencing an issue with branch snapshot comparison where the function appears to be returning `null` instead of finding the common root snapshot between two branches. This is causing problems when trying to merge or compare branches that should have a shared history.

### Reproduction

```js
const branchA = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot3']
};

const branchB = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot4']
};

// This should return 'snapshot2' as the common root
const root = getRootSnapshot(branchA, branchB);
console.log(root); // Returns null instead of 'snapshot2'
```

### Expected behavior

The function should correctly identify and return the most recent common snapshot between two branches. In the example above, it should return `'snapshot2'` since that's the last snapshot shared by both branches before they diverged.

### Additional context

This seems to have started happening recently. The branches definitely share common snapshots in their history, but the comparison logic isn't detecting them properly. This is blocking merge operations between branches with shared ancestry.

---
Repository: /testbed
