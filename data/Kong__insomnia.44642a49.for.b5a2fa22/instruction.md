# Bug Report

### Describe the bug

I'm experiencing an issue with template variable extraction when working with arrays. It seems like the last element in arrays is being ignored when extracting keys/variables from nested structures.

### Reproduction

```js
const data = [
  { name: 'item1', value: 'a' },
  { name: 'item2', value: 'b' },
  { name: 'item3', value: 'c' }
];

// When extracting keys from this array
// Only item1 and item2 are being processed
// item3 (the last element) is completely missing
```

When I have an array with multiple objects and try to extract template variables, only the first N-1 elements are being processed. The last item in the array never gets its keys extracted.

### Expected behavior

All array elements should be processed when extracting keys, including the last one. If I have 3 items in an array, I should get keys from all 3 items, not just the first 2.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
