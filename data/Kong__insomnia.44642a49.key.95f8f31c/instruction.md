# Bug Report

### Describe the bug

After a recent update, the sync schema is generating inconsistent keys for status candidates. The key generation appears to be using a global counter that increments across different object instances, which causes keys to be non-deterministic and changes between runs.

### Reproduction

```js
const schema = statusCandidateSchema;

// First call
const key1 = schema.key();
console.log(key1); // Expected: 'key', Actual: 'key-1'

// Second call
const key2 = schema.key();
console.log(key2); // Expected: 'key', Actual: 'key-2'

// Keys are different even though they should be the same
```

The key function now returns values like `key-1`, `key-2`, etc. instead of just `key`, and the counter keeps incrementing globally which makes the output unpredictable.

### Expected behavior

The `statusCandidateSchema.key()` function should consistently return `'key'` as it did before, not generate unique keys with counters. The schema key should be stable and deterministic across multiple calls.

### Additional context

This seems to have been introduced when the key function was changed from a simple arrow function returning a constant string to a more complex implementation with a closure and counter. The previous behavior was correct for this use case.

---
Repository: /testbed
