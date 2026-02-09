# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict handling where the key generation for merge conflicts is producing inconsistent results. After the first merge conflict is processed, subsequent conflicts are getting different keys (like 'key2', 'key3', etc.) instead of the expected consistent 'key' value.

This is causing problems when trying to resolve multiple merge conflicts in sequence, as the conflict resolution logic expects all conflicts to have the same key structure.

### Reproduction

```js
// Create multiple merge conflicts
const conflict1 = mergeConflictSchema.key();
const conflict2 = mergeConflictSchema.key();
const conflict3 = mergeConflictSchema.key();

console.log(conflict1); // Expected: 'key', Actual: 'key'
console.log(conflict2); // Expected: 'key', Actual: 'key2'
console.log(conflict3); // Expected: 'key', Actual: 'key3'
```

### Expected behavior

All merge conflicts should return the same key value ('key') regardless of how many times the key function is called. The key generation should be stateless and return consistent results.

### System Info

- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
