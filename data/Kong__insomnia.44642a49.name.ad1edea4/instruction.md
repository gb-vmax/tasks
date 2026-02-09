# Bug Report

### Describe the bug

After a recent update, branch name generation is behaving incorrectly. The branch schema appears to be generating sequential names with counters that persist across different contexts, causing unexpected naming collisions and incorrect numbering.

### Reproduction

```js
// Create multiple branches in different projects/contexts
const branch1 = createBranch(); // Expected: 'branch-1'
const branch2 = createBranch(); // Expected: 'branch-2'

// Later, in a completely different context or test
const newBranch = createBranch(); // Expected: 'branch-1', but gets 'branch-3'
```

The counter state seems to be shared globally and never resets, so subsequent branch creations continue incrementing from the previous count even when they shouldn't.

### Expected behavior

Each new context should start with fresh branch naming (e.g., 'branch-1', 'branch-2', etc.). The naming counter should reset between different sessions or contexts, not persist indefinitely.

### Additional context

This is causing issues when creating branches in isolated scenarios where we expect predictable naming. The old behavior just returned an empty string which was more predictable, even if not ideal.

---
Repository: /testbed
