# Bug Report

### Describe the bug

I'm experiencing an issue with the sync delta patching functionality. When applying COPY operations to strings, the resulting patched string is missing characters or has incorrect content. It seems like the patch function is not correctly copying substrings from the original string.

### Reproduction

```js
const original = "Hello World";
const operations = [
  { type: 'COPY', start: 0, len: 5 },  // Should copy "Hello"
  { type: 'INSERT', content: ' ' },
  { type: 'COPY', start: 6, len: 5 }   // Should copy "World"
];

const result = patch(original, operations);
// Expected: "Hello World"
// Actual: Result is missing the first character or has incorrect output
```

### Expected behavior

The patch function should correctly copy substrings from the original string based on the start position and length specified in COPY operations. A COPY operation with `start: 0, len: 5` should copy the first 5 characters from the original string.

### Additional context

This appears to be affecting string synchronization where the delta operations include COPY commands. The patched result doesn't match what it should be when reconstructing strings from operations.

---
Repository: /testbed
