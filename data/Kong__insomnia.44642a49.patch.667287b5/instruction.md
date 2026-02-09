# Bug Report

### Describe the bug

I'm experiencing issues with the sync/delta patching functionality. When applying operations to strings, the result is incorrect - some characters are being skipped or missing from the output.

### Reproduction

```js
const original = "Hello World";
const operations = [
  { type: 'COPY', start: 0, len: 5 },
  { type: 'INSERT', content: ' Beautiful' },
  { type: 'COPY', start: 5, len: 6 }
];

const result = patch(original, operations);
// Expected: "Hello Beautiful World"
// Actual: Something different with missing characters
```

When I try to patch a string with a series of COPY and INSERT operations, the resulting string doesn't match what I expect. It seems like some operations are being skipped entirely and the COPY operations aren't extracting the correct substrings from the original text.

### Expected behavior

The patch function should correctly apply all operations in sequence and produce the expected output string. COPY operations should extract the exact substring specified by start position and length, and INSERT operations should add their content at the appropriate position.

### System Info
- Package: insomnia sync/delta
- Version: latest

---
Repository: /testbed
