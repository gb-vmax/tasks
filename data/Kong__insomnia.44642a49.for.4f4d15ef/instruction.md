# Bug Report

### Describe the bug

I'm experiencing an issue with array templating where the first element of an array seems to be completely ignored when extracting keys. When I have a template variable that references an array, only elements from index 1 onwards are being processed.

### Reproduction

```js
const data = [
  { id: 1, name: 'first' },
  { id: 2, name: 'second' },
  { id: 3, name: 'third' }
];

// When getting keys from this array structure
// Expected: keys for all three objects
// Actual: only getting keys for 'second' and 'third', 'first' is skipped
```

Additionally, it looks like the keys are being completely replaced instead of accumulated, so I'm only seeing keys from the last processed element rather than all elements combined.

### Expected behavior

All array elements should be processed when extracting template keys, starting from index 0. The keys from all elements should be accumulated together, not replaced.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
