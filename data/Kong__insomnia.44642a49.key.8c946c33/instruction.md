# Bug Report

### Describe the bug

I'm encountering an issue with the `mergeConflictSchema` key generation. The schema is generating keys with unexpected prefixes and counters that don't reset properly between uses. This causes problems when trying to identify and track merge conflicts consistently.

### Reproduction

```js
// Create multiple merge conflict objects
const conflict1 = mergeConflictSchema.key();
const conflict2 = mergeConflictSchema.key();
const conflict3 = mergeConflictSchema.key();

// Expected: All should return 'key'
// Actual: Returns 'mc-key', 'mc-key-1', 'mc-key-2' or similar
```

The key generation seems to be using some kind of stack trace inspection and counter that persists across calls, which means:
1. Keys are no longer consistent - they change based on call order
2. The prefix changes from 'key' to 'mc-key' unexpectedly
3. Sequential calls append numbers to the key

### Expected behavior

The `key()` function should return a consistent value (like the original simple `'key'` string) or at minimum should have predictable, documented behavior. The current implementation makes it difficult to work with merge conflicts as their keys keep changing.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
