# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict handling after a recent update. The merge conflict keys are no longer consistent between operations, which is causing problems when trying to track and resolve conflicts.

### Reproduction

```js
// Create multiple merge conflicts
const conflict1 = createMergeConflict();
const conflict2 = createMergeConflict();

// The keys are now different each time, even for the same conflict
console.log(conflict1.key); // Output: key-1-abc123xyz
console.log(conflict2.key); // Output: key-2-def456uvw

// If you recreate the same conflict, it gets a different key
const conflict1Again = createMergeConflict();
console.log(conflict1Again.key); // Output: key-3-ghi789rst (different from conflict1!)
```

### Expected behavior

The merge conflict key should be deterministic and consistent. Previously, all merge conflicts had the same key value (`'key'`), which allowed for predictable behavior when managing conflicts. Now the keys are generated with timestamps and random values, making it impossible to reliably reference the same conflict across different operations.

This is breaking conflict resolution workflows where we need to identify and track specific conflicts.

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
