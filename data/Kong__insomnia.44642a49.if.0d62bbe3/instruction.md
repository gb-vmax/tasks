# Bug Report

### Describe the bug

After a recent update, the VCS branch snapshot comparison is behaving strangely. When trying to find common snapshots between two branches, the function seems to be returning incorrect results or not finding snapshots that should match.

### Reproduction

```js
const branchA = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot3']
};

const branchB = {
  snapshots: ['snapshot1', 'snapshot2', 'snapshot4']
};

// Should return 'snapshot2' as the most recent common snapshot
const rootSnapshot = getRootSnapshot(branchA, branchB);
// But the behavior is inconsistent
```

### Expected behavior

The function should return the most recent common snapshot between two branches. In the example above, it should return `'snapshot2'` since that's the last snapshot they both share.

### Additional context

This seems to have started happening recently. The snapshot comparison logic appears to have changed and now produces unexpected results when comparing branch histories. Sometimes it works, sometimes it doesn't find the common snapshot even when one clearly exists.

Not sure if this is related to some caching mechanism or if the comparison algorithm itself has issues.

---
Repository: /testbed
