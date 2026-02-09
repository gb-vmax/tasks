# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict schema generation where the `message` field returns inconsistent values across multiple calls. The first call returns `'message'` but subsequent calls return `'message '` (with a trailing space).

### Reproduction

```js
const schema = mergeConflictSchema;

// First call
const msg1 = schema.message();
console.log(msg1); // Output: 'message'

// Second call
const msg2 = schema.message();
console.log(msg2); // Output: 'message ' (note the trailing space)

// These values should be identical but they're not
console.log(msg1 === msg2); // false
```

### Expected behavior

The `message()` function should return the same value consistently on every call, just like the other schema fields (`name()`, `mineBlobContent()`, etc.). All calls should return `'message'` without any trailing spaces or variation.

### System Info
- Package: insomnia/sync
- Version: latest

---
Repository: /testbed
